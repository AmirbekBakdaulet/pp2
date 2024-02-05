class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x, self.y)
    def dist(self,x2, y2):
        self.x2=x2
        self.y2=y2
        d=((self.x-self.x2)**2 +(self.y - self.y2)**2)**0.5
        print(f"distance is {d}")
    def change(self, dx, dy):
        self.x+=dx
        self.y+=dy
        print(self.x, self.y)
    
x=int(input("x:"))
y=int(input("y:"))
p=Point(x,y)
p.show()
x2=int(input("x2:"))
y2=int(input("y2:"))
p.dist(x2,y2)
dx=int(input("dx:"))
dy=int(input("dy:"))
p.change(dx,dy)