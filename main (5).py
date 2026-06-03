import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius*self.radius
    def perimeter(self):
        return 2*math.pi*self.radius
class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        s=(self.a+self.b+self.c)/2
        return math.sqrts(s*(s-self.a)*(s-self.b)*(s-self.c))
    def perimeter(self):
        return self.a+self.b+self.c
print("1.Rectangle")
print("2.Circle")
print("3.Triangle")
choice=int(input("Enter your choice: "))
if choice==1:
    length=float(input("enter length: "))
    width=float(input("enter width: "))
    obj=Rectangle(length,width)
    print("Area:",obj.area())
    print("Perimeter:",obj.perimeter())
elif choice==2:
    radius=float(input("Enter length:"))
    
    obj=Circle(radius)
    print("Area:",obj.area())
    print("Perimeter: ",obj.perimeter())
elif choice==3:
    a=float(input("Enter side 1: "))
    b=float(input("Enter side 2: "))
    c=float(input("Enter side 3: "))
    obj= Triangle(a,b,c)
    print("Area: ",obj.area())
    print("Perimeter: ",obj.perimeter())
else:
    print("Invalid choice")