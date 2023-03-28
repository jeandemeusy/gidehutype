import unittest

from gidehutype import Dict, SizedDict


class TestStructure:
    all = Dict("foo")
    sized = SizedDict("bar", maxlen=10)


class TestDict(unittest.TestCase):
    inst = TestStructure()

    def test_is_dict(self):
        wrong_values = [1, 1.0, "foo", True, [1, 2, 3], (1, 2, 3), {1, 2, 3}, None]
        good_values = [{1: 2, 3: 4}]
        
        for v in wrong_values:
            with self.assertRaises(TypeError):
                TestDict.inst.all = v

        for v in good_values:
            TestDict.inst.all = v

    def test_is_sized(self):
        with self.assertRaises(ValueError):
            TestDict.inst.sized = {val: val for val in range(20)}

        TestDict.inst.sized = {val: val for val in range(5)}
    

if __name__ == '__main__':
    unittest.main()