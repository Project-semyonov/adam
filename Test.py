class Test:
    def __init__(self):
        self.dummy = ""

    def printer(self):
        self.dummy = "Hello World!"
        print(self.dummy)

if __name__ == '__main__':
    foo = Test()
    foo.printer()
