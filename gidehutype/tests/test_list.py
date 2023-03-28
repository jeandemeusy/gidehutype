import unittest

from gidehutype import (BoolList, ComplexList, FloatList, IntegerList, List,
                        SizedBoolList, SizedComplexList, SizedFloatList,
                        SizedIntegerList, SizedList, SizedStringList,
                        StringList)


class TestStructure:
    all = List("foo")
    bool = BoolList("bar")
    complex = ComplexList("baz")
    float = FloatList("qux")
    integer = IntegerList("quux")
    string = StringList("quuz")
    sizedAll = SizedList("corge", maxlen=3)
    sizedBool = SizedBoolList("grault", maxlen=3)
    sizedComplex = SizedComplexList("garply", maxlen=3)
    sizedFloat = SizedFloatList("waldo", maxlen=3)
    sizedInteger = SizedIntegerList("fred", maxlen=3)
    sizedString = SizedStringList("plugh", maxlen=3)


class TestList(unittest.TestCase):
    inst = TestStructure()

    def test_is_list(self):
        wrong_values = [1, 1.0, "foo", True, (1, 2, 3), {1, 2, 3}, {1: 2, 3: 4}, None]
        good_values = [[1, "2", 3.0]]


        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestList.inst.all = v
        
        for v in good_values:
            TestList.inst.all = v

    def test_is_sized(self):
        with self.assertRaises(ValueError):
            TestList.inst.sizedAll = [1, 2, 3, 4]

        TestList.inst.sized = [1, 2]

    def test_is_bool(self):
        wrong_values = [
            [1, 2, 3],
            [1.0, 2.0, 3.0],
            [1j, 2j, 3j],
            ["foo", "bar", "baz"],
            [(1, 2, 3), (4, 5, 6), (7, 8, 9)],
            {1: 2, 3: 4},
            None
        ]
        good_values = [[True, False, True]]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestList.inst.bool = v

        for v in good_values:
            TestList.inst.bool = v

    def test_is_sized_bool(self):
        with self.assertRaises(ValueError):
            TestList.inst.sizedBool = [True, False, True, False]

        TestList.inst.sizedBool = [True, False, True]

    def test_is_complex(self):
        wrong_values = [
            [1, 2, 3],
            [1.0, 2.0, 3.0],
            [True, False, True],
            ["foo", "bar", "baz"],
            [(1, 2, 3), (4, 5, 6), (7, 8, 9)],
            {1: 2, 3: 4},
            None
        ]
        good_values = [[1j, 2j, 3j]]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestList.inst.complex = v

        for v in good_values:
            TestList.inst.complex = v

    def test_is_sized_complex(self):
        with self.assertRaises(ValueError):
            TestList.inst.sizedComplex = [1j, 2j, 3j, 4j]

        TestList.inst.sizedComplex = [1j, 2j, 3j]
    
    def test_is_float(self):
        wrong_values = [
            [1, 2, 3],
            [1j, 2j, 3j],
            [True, False, True],
            ["foo", "bar", "baz"],
            [(1, 2, 3), (4, 5, 6), (7, 8, 9)],
            {1: 2, 3: 4},
            None
        ]
        good_values = [[1.0, 2.0, 3.0]]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestList.inst.float = v

        for v in good_values:
            TestList.inst.float = v

    def test_is_sized_float(self):
        with self.assertRaises(ValueError):
            TestList.inst.sizedFloat = [1.0, 2.0, 3.0, 4.0]

        TestList.inst.sizedFloat = [1.0, 2.0, 3.0]

    def test_is_integer(self):
        wrong_values = [
            [1.0, 2.0, 3.0],
            [1j, 2j, 3j],
            ["foo", "bar", "baz"],
            [(1, 2, 3), (4, 5, 6), (7, 8, 9)],
            {1: 2, 3: 4},
            None
        ]
        good_values = [[1, 2, 3]]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestList.inst.integer = v

        for v in good_values:
            TestList.inst.integer = v

    def test_is_sized_integer(self):
        with self.assertRaises(ValueError):
            TestList.inst.sizedInteger = [1, 2, 3, 4]

        TestList.inst.sizedInteger = [1, 2, 3]

    def test_is_string(self):
        wrong_values = [
            [1, 2, 3],
            [1.0, 2.0, 3.0],
            [1j, 2j, 3j],
            [True, False, True],
            [(1, 2, 3), (4, 5, 6), (7, 8, 9)],
            {1: 2, 3: 4},
            None
        ]
        good_values = [["foo", "bar", "baz"]]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestList.inst.string = v

        for v in good_values:
            TestList.inst.string = v

    def test_is_sized_string(self):
        with self.assertRaises(ValueError):
            TestList.inst.sizedString = ["foo", "bar", "baz", "qux"]

        TestList.inst.sizedString = ["foo", "bar", "baz"]
    

if __name__ == '__main__':
    unittest.main()