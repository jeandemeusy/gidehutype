import unittest

from gidehutype import SizedString, String


class TestStructure:
    all = String("foo")
    sized = SizedString("bar", maxlen=10)

class TestString(unittest.TestCase):
    inst = TestStructure()

    def test_is_string(self):
        wrong_values = [
            1,
            1.0,
            True,
            [1, 2, 3],
            (1, 2, 3),
            {1, 2, 3},
            {1: 2, 3: 4},
            None
        ]
        good_values = ["foo", "bar", "baz"]

        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestString.inst.all = v

        for v in good_values:
            TestString.inst.all = v
            
    def test_is_sized(self):
        with self.assertRaises(ValueError):
            TestString.inst.sized = "0"*20

        TestString.inst.sized = "0"*5

if __name__ == '__main__':
    unittest.main()