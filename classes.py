from datetime import date
#calculate area and perimeter of a circle
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius

circle_1=Circle(2)

r_1=circle_1.area()
r_2=circle_1.perimeter()
print (r_1)
print(r_2)


#calculate age of a person
class Person():
    def __init__(self,name, date_of_birth,country):
        self.name=name
        self.date_of_birth=date_of_birth
        self.country=country
    def age(self):

        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
         age -= 1
        return age





person1=Person("Felix",date(1962, 7, 12),"Canada")
print(person1.age())
print("name:" , person1.name)

#create a class calculator
class Calculator:
    def __init__(self,param):
        self.a=param[0]
        self.b=param[1]
    def add (self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        if  self.b!= 0:
            return self.a/self.b
        else:
            return "cannot be divided"


calculate=Calculator((1,2))
print(calculate.add())
print(calculate.sub())
print(calculate.multiply())
print(calculate.divide())

#class for different shapes
class Shape:
    def __init__(self):
        pass
class Circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius
class Triangle():
    def __init__(self,b,h):
        self.b=b
        self.h=h
    def area(self):
        return 0.5 * self.b * (self.h)**2
    def perimeter(self):
        pass
class Square():
    def __init__(self,a):
        self.a=a


    def area(self):
        return self.a *self.a
    def perimeter(self):
        return 2 * self.a

triangle=Triangle(1,2)
print(triangle.area())