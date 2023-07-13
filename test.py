class A(object):
    def __add__(self):
        print("I am test in A")


if __name__ == '__main__':
   a=A();
   a.__add__();