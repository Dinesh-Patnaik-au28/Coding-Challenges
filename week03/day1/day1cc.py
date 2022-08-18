#Write a function which will take a str as input and will return a string
#where vowels are removed.


def vowel(string):
    v = ("A","E","I","O","U")
    for i in string:
        for i in v:
            string = string.replace(i, "")
            print(string)
            return string
vowel("ABCDEFG")

#What will be the output

def printMax(a, b):
  if a > b:
    print(a, 'is maximum')
  elif a == b:
          print(a, 'is equal to', b)
  else:
        print(b, 'is maximum')
        printMax(3, 4)


x = 50
def func(x):
     print('x is', x)
x = 2
print('Changed local x to', x)
func(x)
print('x is now', x)      #Write a function that returns(not prints) the data-type of the last
#element in a list
def list(items):
    l1=type(items[-1])
    return 11
l2 = [ "Dinesh"," Odisha" 54,36]
print(list(l2))