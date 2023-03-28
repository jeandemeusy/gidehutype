import unittest

from gidehutype import Complex


class TestStructure:
    all = Complex("foo")

class TestComplex(unittest.TestCase):
    inst = TestStructure()

    def test_is_complex(self):
        wrong_values = [
            1, 1.0, "foo", True, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 2, 3: 4}, None
        ]

        good_values = [1 + 1j]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestComplex.inst.all = v
            
        for v in good_values:
            TestComplex.inst.neg = v

if __name__ == '__main__':
    unittest.main()