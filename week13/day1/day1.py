#In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and
#classes in programming. It aims to implement real-world entities like inheritance, polymorphisms,
#encapsulation, etc. in the programming. The main concept of OOPs is to bind the data and the
#functions that work on that together as a single unit so that no other part of the code can access this data.
#Class
#Objects
#The __init__ method
#Types of method
#Inheritance
#Constructor in inheritance
#Encapsulation
class laptop:
    def config(self):
        print("i5, 08gb")
lap1 = laptop()
laptop.config(lap1)
#------------# (Class And Objects)
class laptop:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("config is ", self.cpu, self.ram)
lap1 = laptop("i5" , 8)
lap2 = laptop("i7", 12)
lap1.config()
lap2.config()
#------------# (The __init__ method)
class student:
    school = "dhamaka"
    def __init__(self,mar1,mar2):
        self.mar1=mar1
        self.mar2=mar2
    def avg(self):
        return (self.mar1 + self.mar2)/2
    def get_mar1(self):
        return self.mar1
    def set_mar1(self,value):
        self.m1 = value
    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        print("this ia keybord class")    
std1 = student(22,11)
std2 = student(17,56)
print(std1.avg())
print(std2.avg())
print(student.getschool())
student.info()
#------------# (Types of method)
class A:
    def cric1(self):
        print("cric 1 is good")
    def cric2(self):
        print("cric 2 is good")
class B(A):
    def foot1(self):
        print("foot 1 is ok")
    def foot2(self):
        print("foot 2 is ok")
class C(B):
    def bass1(self):
        print("bass 1 is best")
    def bass2(self):
        print("bass 2 is best")
ply1 = A()
ply2 = B()
ply3 = C()
ply1.cric1()
ply2.foot1()
ply3.bass1()
#------------# (Inheritance And Multi Inheritance)
class A:
    def __init__(self):
        print("india is best in cricket")
    def cric1(self):
        print("cric 1 is good")
    def cric2(self):
        print("cric 2 is good")
class B(A):
    def __init_(self):
        super.__init__()
        print("argentina is ok football")
    def foot1(self):
        print("foot 1 is ok")
    def foot2(self):
        print("foot 2 is ok")
class C(B):
    def __init__(self):
        print("usa is best in bassket ball")
    def bass1(self):
        print("bass 1 is best")
    def bass2(self):
        print("bass 2 is best")
ply1 = A()
ply2 = B()
ply3 = C()
ply1.cric1()
ply2.foot1()
ply3.bass1()
#------------# (Constructor in inheritance)
class payment:
    def __init__(self, price):
        self.__final_price = price + price*0.05
    def get_final_price(self):
        return self.__final_price
    def set_final_price(self,discount):
        if __name__ == "__main__":
            self.__final_price = self.__final_price - self.__calculate_discount(discount)
    def __calculate_discount(self, discount):
        return self.__final_price * (discount/100)
computer = payment(40000)
computer.set_final_price(10)
print(computer.get_final_price())
#------------# (Encapsulation)
class Bird:
	def intro(self):
		print("There are many types of birds.")
	def flight(self):
		print("Most of the birds can fly but some cannot.")
class sparrow(Bird):
	def flight(self):
		print("Sparrows can fly.")
class ostrich(Bird):
	def flight(self):
		print("Ostriches cannot fly.")
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
obj_bird.intro()
obj_bird.flight()
obj_spr.intro()
obj_spr.flight()
obj_ost.intro()
obj_ost.flight()
#------------# (Polymorphism)
from abc import ABC, abstractmethod
class Polygon(ABC):
	@abstractmethod
	def noofsides(self):
		pass
class Triangle(Polygon):
	def noofsides(self):
		print("I have 3 sides")
class Pentagon(Polygon):
	def noofsides(self):
		print("I have 5 sides")
class Hexagon(Polygon):
	def noofsides(self):
		print("I have 6 sides")
class Quadrilateral(Polygon):
	def noofsides(self):
		print("I have 4 sides")
R = Triangle()
R.noofsides()
K = Quadrilateral()
K.noofsides()
R = Pentagon()
R.noofsides()
K = Hexagon()
K.noofsides()
#------------# (Abstraction)