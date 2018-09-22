import unittest

class prove_works:
    def __init__(self):
        self.dummy = ""

    def printer(self):
        self.dummy = "Hello World!"
        print(self.dummy)

    def mirror(self, num):
        return num

class test_test(unittest.TestCase):
    
    def test_one(self):
        foo = prove_works()
        self.assertEqual(foo.mirror(1), 1)
        self.assertEqual(foo.mirror(1), 2)

if __name__ == '__main__':
    unittest.main()
    foo = prove_works()
    foo.printer()
