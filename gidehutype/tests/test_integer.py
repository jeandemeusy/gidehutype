import unittest

from gidehutype import (Integer, NegativeInteger, PositiveInteger,
                        RestrictedInteger, StrictNegativeInteger,
                        StrictPositiveInteger)


class TestStructure:
    neg = NegativeInteger("foo")
    pos = PositiveInteger("bar")
    all = Integer("baz")
    res = RestrictedInteger("qux", minval = 0, maxval = 10)
    strNeg = StrictNegativeInteger("quux")
    strPos = StrictPositiveInteger("quuz")

class TestInteger(unittest.TestCase):
    inst = TestStructure()

    def test_is_integer(self):
        wrong_values = [1.0, "foo", [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 2, 3: 4}, None]
        good_values = [1]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestInteger.inst.all = v

        for v in good_values:
            TestInteger.inst.all = v

    def test_is_negative(self):
        with self.assertRaises(ValueError):
            TestInteger.inst.neg = 1

        TestInteger.inst.neg = -1

    def test_is_positive(self):
        with self.assertRaises(ValueError):
            TestInteger.inst.pos = -1

        TestInteger.inst.pos = 1

    def test_is_restricted(self):
        with self.assertRaises(ValueError):
            TestInteger.inst.res = 11
        
        TestInteger.inst.res = 5

    def test_is_strict_negative(self):
        with self.assertRaises(ValueError):
            TestInteger.inst.strNeg = 0
    
        TestInteger.inst.strNeg = -1

    def test_is_strict_positive(self):
        with self.assertRaises(ValueError):
            TestInteger.inst.strPos = 0

        TestInteger.inst.strPos = 1

if __name__ == '__main__':
    unittest.main()