import unittest

from gidehutype import (Float, NegativeFloat, PositiveFloat, RestrictedFloat,
                        StrictNegativeFloat, StrictPositiveFloat)


class TestStructure:
    neg = NegativeFloat("foo")
    pos = PositiveFloat("bar")
    all = Float("baz")
    res = RestrictedFloat("qux", minval = 0.0, maxval = 10.0)
    strNeg = StrictNegativeFloat("quux")
    strPos = StrictPositiveFloat("quuz")

class TestFloat(unittest.TestCase):
    inst = TestStructure()

    def test_is_float(self):
        wrong_values = [1, "foo", True, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 2, 3: 4}, None]
        good_values = [1.0]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestFloat.inst.all = v

        for v in good_values:
            TestFloat.inst.all = v

    def test_is_negative(self):
        with self.assertRaises(ValueError):
            TestFloat.inst.neg = 1.0

        TestFloat.inst.neg = -1.0

    def test_is_positive(self):
        with self.assertRaises(ValueError):
            TestFloat.inst.pos = -1.0

        TestFloat.inst.pos = 1.0

    

    def test_is_restricted(self):
        with self.assertRaises(ValueError):
            TestFloat.inst.res = 11.0
        
        TestFloat.inst.res = 5.0

    def test_is_strict_negative(self):
        with self.assertRaises(ValueError):
            TestFloat.inst.strNeg = 0.0
    
        TestFloat.inst.strNeg = -1.0

    def test_is_strict_positive(self):
        with self.assertRaises(ValueError):
            TestFloat.inst.strPos = 0.0

        TestFloat.inst.strPos = 1.0

if __name__ == '__main__':
    unittest.main()