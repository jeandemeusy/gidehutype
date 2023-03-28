import unittest

from gidehutype import Bool


class TestStructure:
    all = Bool("foo")

class TestBool(unittest.TestCase):
    inst = TestStructure()

    def test_is_bool(self):
        wrong_values = [
            1, 1.0, "foo", [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 2, 3: 4}, None
        ]
        good_values = [True, False]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestBool.inst.all = v

        for v in good_values:
            TestBool.inst.all = v

if __name__ == '__main__':
    unittest.main()