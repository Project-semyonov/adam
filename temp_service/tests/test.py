import unittest
from temp_service.source import example
class Test_example(unittst.TestCase):
    def test_one(self):
        self.assertEqual(example.mirror(1), 1)

if __name__=='__main__':
    unittest.main()
