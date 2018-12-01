import unittest
from ..source_files.endpoint import Temp

class Test1(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pass(self):
        assert True

    def test_class(self):
        tem = Temp()
        
        assert tem


if __name__ == '__main__':
    unittest.main()

