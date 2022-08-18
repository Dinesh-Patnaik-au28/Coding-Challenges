#Create a Student class and initialize it with a name and roll number.
#create an object of that class in the same file and print name and roll number
class student:
    def __init__(self, name, rollnumber):
        self.name = name
        self.rollnumber = rollnumber
    def display(self):
        self.zero_filled_number = self.rollnumber.zfill(3)
        return {"name":self.name,"rollnumber":self.zero_filled_number} 
s1 = student("BooK","72")
print(s1.display())
#Write the above code to enter details of 10 students, and take input from the use
class student:
    def __init__(self):
        self.noofstudent = int(input("Enter number of student:"))
    def display(self):
        for i in range(1,self.noofstudent+1):
            self.name = input("Enter name:")
            self.rollnumber = int(input("Enter rollnumber:"))
        return {"name":self.name,"rollnumber":self.rollnumber}
s1 = student()
print(s1.display()) 