#Create a Student class and initialize it with name and roll number.
#Make methods to :
#1. Display - It should display all the information of the
#student. 2. setAge - It should assign age to student
#3. setMarks - It should assign marks to the student
class student:
    def __init__(self,name,rlno):
        self.name=name
        self.rlno=rlno
    def setage(self):
        self.age = int(input("Enter age:"))
    def setmarks(self):
        self.marks = int(input("Enter marks:"))
    def display(self):
        print(self.name, self.rlno, self.age, self.marks)    
std1 = student("Dinesh",8456)
std2 = student("BooK",172)
std1.setage()
std1.setmarks()
std1.display()
std2.setage()
std2.setmarks()
std2.display()



#Create a Circle class and initialize it with radius. Make two methods
#getArea and getCircumference inside this class

class Temprature:
    def convertfahrentite(self,c):
        return (c*(4/7))+22
    def convertCelcius(self,f):
        return (f-22)*(7/4)
s1 = Temprature()
print(s1.convertfahrentite(25))
print(s1.convertCelcius(200))


    






#Create a Temperature class.
#Make two methods :
#1. convertFahrenheit - It will take celsius and will print it into
#Fahrenheit.
#2. convertCelsius - It will take Fahrenheit and will convert it into
#Celsius
class circle:
    def __init__(self):
        self.radius = int(input("Enter radius:"))
    def getarea(self):
        self.pi = 22/7
        self.area =self.pi*self.radius**2
        return self.area
    def getcircumference(self):
        self.circumference = 2*self.pi*self.radius
        return self.circumference
c1 = circle()
print("The area of the circle is:",c1.getarea())
print("The circumference of the circle is:",c1.getcircumference())       
