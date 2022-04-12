import unittest
from context import randomiser

class RandomiserTestCase(unittest.TestCase):

    def test_1_range_check(self):
        self.assertIn(randomiser(start=1,end=26),list(range(1,27)))
    
    def test_2_single_exclusion(self):
        self.assertEqual(randomiser(2,start=1,end=2),1)
    
    def test_3_multi_exclusions(self):
        self.assertEqual(randomiser(1,2,start=1,end=3),3)

if __name__ == '__main__':
    unittest.main()