class A(object):
    pass

if __name__ == '__main__':
    a = A()
    b = A()

    print(id(a))
    print(id(a) == id(b)) # False
    print(a)  # <__main__.A object at 0x00000198A3678700>
    print(b)  # <__main__.A object at 0x00000198A36A89D0>

