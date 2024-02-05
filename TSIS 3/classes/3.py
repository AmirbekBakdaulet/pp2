from area import shape
class rectungle(shape):
    def __init__(self, len, wid):
        super().__init__()
        self.length = len
        self.width = wid
    def area(self):
        print(self.length * self.width)
len=float(input("length:"))
wid=float(input("width:"))
tri=rectungle(len, wid)
tri.area()
    