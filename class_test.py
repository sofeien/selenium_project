class A():
    x=1
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b

i=A(2,3)
i.x=2
print(A.x,i.x)
