import unittest

class Test:
    def __init__(self):
        self.dummy = ""

    def printer(self):
        self.dummy = "Hello World!"
        print(self.dummy)

    def mirror(self, num):
        return num

class test_test(unittest.TestCase):
    
    def one_test(self):
        foo = Test()
        self.assertEqual(g.mirror(1), 1)

if __name__ == '__main__':
    foo = Test()
    foo.printer()
