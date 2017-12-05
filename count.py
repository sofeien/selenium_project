class Count:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b

if __name__=="__main__":
    assert Count().add(2,3)==5
    assert Count().sub(3,1)==2
    print("OK")
