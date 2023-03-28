import unittest

from gidehutype import (BoolTuple, ComplexTuple, FloatTuple, IntegerTuple,
                        SizedBoolTuple, SizedComplexTuple, SizedFloatTuple,
                        SizedIntegerTuple, SizedStringTuple, SizedTuple,
                        StringTuple, Tuple)


class TestStructure:
    all = Tuple("foo")
    bool = BoolTuple("bar")
    complex = ComplexTuple("baz")
    float = FloatTuple("qux")
    integer = IntegerTuple("quux")
    string = StringTuple("quuz")
    sizedAll = SizedTuple("corge", maxlen=3)
    sizedBool = SizedBoolTuple("grault", maxlen=3)
    sizedComplex = SizedComplexTuple("garply", maxlen=3)
    sizedFloat = SizedFloatTuple("waldo", maxlen=3)
    sizedInteger = SizedIntegerTuple("fred", maxlen=3)
    sizedString = SizedStringTuple("plugh", maxlen=3)


class TestTuple(unittest.TestCase):
    inst = TestStructure()

    def test_is_tuple(self):
        wrong_values = [1, 1.0, "foo", True, [1, 2, 3], {1, 2, 3}, {1: 2, 3: 4}, None]
        good_values = [(1, "2", 3.0)]


        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestTuple.inst.all = v
        
        for v in good_values:
            TestTuple.inst.all = v

    def test_is_sized(self):
        with self.assertRaises(ValueError):
            TestTuple.inst.sizedAll = (1, 2, 3, 4)

        TestTuple.inst.sized = (1, 2)

    def test_is_bool(self):
        wrong_values = [
            (1, 2, 3),
            (1.0, 2.0, 3.0),
            (1j, 2j, 3j),
            ("foo", "bar", "baz"),
            ((1, 2, 3), (4, 5, 6), (7, 8, 9)),
        ]
        good_values = [(True, False, True)]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestTuple.inst.bool = v

        for v in good_values:
            TestTuple.inst.bool = v

    def test_is_sized_bool(self):
        with self.assertRaises(ValueError):
            TestTuple.inst.sizedBool = (True, False, True, False)

        TestTuple.inst.sizedBool = (True, False, True)

    def test_is_complex(self):
        wrong_values = [
            (1, 2, 3),
            (1.0, 2.0, 3.0),
            (True, False, True),
            ("foo", "bar", "baz"),
            ((1, 2, 3), (4, 5, 6), (7, 8, 9)),
            ({1: 2, 3: 4}),
        ]
        good_values = [(1j, 2j, 3j)]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestTuple.inst.complex = v

        for v in good_values:
            TestTuple.inst.complex = v

    def test_is_sized_complex(self):
        with self.assertRaises(ValueError):
            TestTuple.inst.sizedComplex = (1j, 2j, 3j, 4j)

        TestTuple.inst.sizedComplex = (1j, 2j, 3j)
    
    def test_is_float(self):
        wrong_values = [
            (1, 2, 3),
            (1j, 2j, 3j),
            (True, False, True),
            ("foo", "bar", "baz"),
            ((1, 2, 3), (4, 5, 6), (7, 8, 9)),
            ({1: 2, 3: 4}),
        ]
        good_values = [(1.0, 2.0, 3.0)]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestTuple.inst.float = v

        for v in good_values:
            TestTuple.inst.float = v

    def test_is_sized_float(self):
        with self.assertRaises(ValueError):
            TestTuple.inst.sizedFloat = (1.0, 2.0, 3.0, 4.0)

        TestTuple.inst.sizedFloat = (1.0, 2.0, 3.0)

    def test_is_integer(self):
        wrong_values = [
            (1.0, 2.0, 3.0),
            (1j, 2j, 3j),
            ("foo", "bar", "baz"),
            ((1, 2, 3), (4, 5, 6), (7, 8, 9)),
            ({1: 2, 3: 4}),
        ]
        good_values = [(1, 2, 3)]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestTuple.inst.integer = v

        for v in good_values:
            TestTuple.inst.integer = v

    def test_is_sized_integer(self):
        with self.assertRaises(ValueError):
            TestTuple.inst.sizedInteger = (1, 2, 3, 4)

        TestTuple.inst.sizedInteger = (1, 2, 3)

    def test_is_string(self):
        wrong_values = [
            (1, 2, 3),
            (1.0, 2.0, 3.0),
            (1j, 2j, 3j),
            (True, False, True),
            ((1, 2, 3), (4, 5, 6), (7, 8, 9)),
            ({1: 2, 3: 4}),
        ]
        good_values = [("foo", "bar", "baz")]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestTuple.inst.string = v

        for v in good_values:
            TestTuple.inst.string = v

    def test_is_sized_string(self):
        with self.assertRaises(ValueError):
            TestTuple.inst.sizedString = ("foo", "bar", "baz", "qux")

        TestTuple.inst.sizedString = ("foo", "bar", "baz")
    

if __name__ == '__main__':
    unittest.main()