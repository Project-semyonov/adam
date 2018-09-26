class prove_works:
    def __init__(self):
        self.dummy = ""

    def printer(self):
        self.dummy = "Hello World!"
        print(self.dummy)

    def mirror(self, num):
        return num

if __name__ == '__main__':
    foo = prove_works()
    foo.printer()
