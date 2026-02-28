# class student :
#     name = "harsh"
    
# s1 = student()
# print(s1.name)


# class car:
#     color = "blue"
#     brand = "mercedis"
    
# car1 = car()
# print(car.color)
# print(car.brand)

# __init__ mate

class student :
    college_name = "ahmedabad institut of tecnology"
    # name = "kuldeep" #class attr 
    def __init__(self,name,mark):
        self.name = name  #obj attr > class attr   atla mate kuldeep print nai thay 
        self.mark = mark
    @staticmethod   #decorder ama self no use na thay
    def hello():
        print("hello")
    def welcome (self):
        print("welcome student",self.name,"and your mark is:",self.mark)
    def get_mark (self):
        return self.mark
        # print("adding student in data base")
    # name = "harsh"

s1 = student("harsh",98)   #atribute kevay je data ne apde stor kar vi tene 
# print(s1.name,s1.mark)
s1.welcome()
s1.hello()
print(s1.get_mark())
print(s1.college_name)

s2 = student("ekta",80)
print(s2.get_mark())
print(s2.college_name)