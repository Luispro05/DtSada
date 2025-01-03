class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def __eq__(self, outro):
        return self.x == outro.x

class B:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def __eq__(self, outro):
        return self.y == outro.y

a = A(x=1, y=2)
b = B(x=1, y=3)
print(a==b, b==a)