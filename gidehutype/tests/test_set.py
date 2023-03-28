import unittest

from gidehutype import (BoolSet, ComplexSet, FloatSet, IntegerSet, Set,
                        SizedBoolSet, SizedComplexSet, SizedFloatSet,
                        SizedIntegerSet, SizedSet, SizedStringSet, StringSet)


class TestStructure:
    all = Set("foo")
    bool = BoolSet("bar")
    complex = ComplexSet("baz")
    float = FloatSet("qux")
    integer = IntegerSet("quux")
    string = StringSet("quuz")
    sizedAll = SizedSet("corge", maxlen=3)
    sizedBool = SizedBoolSet("grault", maxlen=1)
    sizedComplex = SizedComplexSet("garply", maxlen=3)
    sizedFloat = SizedFloatSet("waldo", maxlen=3)
    sizedInteger = SizedIntegerSet("fred", maxlen=3)
    sizedString = SizedStringSet("plugh", maxlen=3)


class TestSet(unittest.TestCase):
    inst = TestStructure()

    def test_is_set(self):
        wrong_values = [
            1,
            1.0,
            "foo",
            True,
            [1, 2, 3],
            (1, 2, 3),
            {1: 2, 3: 4}
        ]
        good_values = [{1, 2, 3}, {1.0, 2.0, 3.0}, {"foo", "bar", "baz"}]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestSet.inst.all = v

        for v in good_values:
            TestSet.inst.all = v

    def test_is_sized(self):
        with self.assertRaises(ValueError):
            TestSet.inst.sizedAll = {1, 2, 3, 4}

        TestSet.inst.sized = {1, 2}

    def test_is_bool(self):
        wrong_values = [
            {1},
            {1.0},
            {"foo"},
            {(1, 2, 3)},
            {1j},
        ]
        good_values = [{True, False}]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestSet.inst.bool = v
        
        for v in good_values:
            TestSet.inst.bool = v

    def test_is_sized_bool(self):
        with self.assertRaises(ValueError):
            TestSet.inst.sizedBool = {True, False}

        TestSet.inst.sizedBool = {True}

    def test_is_complex(self):
        wrong_values = [
            {1},
            {1.0},
            {"foo"},
            {(1, 2, 3)},
        ]
        good_values = [{1j, 2j, 3j}]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestSet.inst.complex = v

        for v in good_values:
            TestSet.inst.complex = v

    def test_is_sized_complex(self):
        with self.assertRaises(ValueError):
            TestSet.inst.sizedComplex = {1j, 2j, 3j, 4j}

        TestSet.inst.sizedComplex = {1j, 2j, 3j}
    
    def test_is_float(self):
        wrong_values = [
            {1},
            {"foo"},
            {(1, 2, 3)},
            {1j},
            None
        ]
        good_values = [{1.0, 2.0, 3.0}]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestSet.inst.float = v

        for v in good_values:
            TestSet.inst.float = v

    def test_is_sized_float(self):
        with self.assertRaises(ValueError):
            TestSet.inst.sizedFloat = {1.0, 2.0, 3.0, 4.0}

        TestSet.inst.float = {1.0, 2.0, 3.0}

    def test_is_integer(self):
        wrong_values = [
            {1.0},
            {"foo"},
            {(1, 2, 3)},
            {1j}
        ]
        good_values = [{1, 2, 3}]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestSet.inst.integer = v

        for v in good_values:
            TestSet.inst.integer = v

    def test_is_sized_integer(self):
        with self.assertRaises(ValueError):
            TestSet.inst.sizedInteger = {1, 2, 3, 4}

        TestSet.inst.sizedInteger = {1, 2, 3}

    def test_is_string(self):
        wrong_values = [
            {1},
            {1.0},
            {(1, 2, 3)},
            {1j},
        ]
        good_values = [{"foo", "bar", "baz"}]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestSet.inst.string = v
        
        for v in good_values:
            TestSet.inst.string = v

    def test_is_sized_string(self):
        with self.assertRaises(ValueError):
            TestSet.inst.sizedString = {"foo", "bar", "baz", "qux"}

        TestSet.inst.sizedString = {"foo", "bar", "baz"}
    

if __name__ == '__main__':
    unittest.main()