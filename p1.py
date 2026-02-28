# def squar (a):
#     multiply = a*a
#     return multiply

# print(squar(2)) 
# print(squar(3))

# sum of avg 

# def avg (a,b,c):
#     sum = a+b+c
#     avg = sum /3 
#     return  avg
# print(avg(1,2,3))
# print(avg(3,3,3))

# find max number

# def findmax(numbers):
#      return max(numbers)
 
# list = [10,20,30,40,50,60]

# print ("the maximum number is :", findmax(list))

# file = open("demo.txt", "w")
# file.write("Hello File Handling")
# file.close()

class Student:
    def __init__(self, name):
        self._name = name

class Child(Student):
    def show(self):
        print(self._name)

c = Child("Harsh")
c.show()
