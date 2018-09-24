import unittest
from .example import prove_works
class Test_example(unittest.TestCase):
    def test_one(self):
        example = prove_works()
        self.assertEqual(example.mirror(1), 1)

if __name__=='__main__':
    unittest.main()
