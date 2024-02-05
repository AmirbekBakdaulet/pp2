class shape:
    def area(self):
        print(0)
class square(shape):
    def __init__(self,len):
        self.len=len
    def area(self):
        self.a=self.len**2
        print(self.a)
len=float(input())
kvadrat=square(len)
kvadrat.area()
shar=shape()
shar.area()
