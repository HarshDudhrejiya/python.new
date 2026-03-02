# class student():
#     def __init__(self,name):
#         self.name = name
#         # self.__name = name  #__ lagavathi private bani jai che 
        
        
# s1 = student("harsh")
# # print(s1.__name)
# del s1
# print(s1.name)



# class person():
#     __name = "harsh"
#     def __hello(self):
#         print("hello person")
#     def welcome(self):
#         self.__hello()
        
# p1 = person()
# print(p1.welcome())




#inherit karva mate ****

# class car():
#     @staticmethod
#     def start ():
#         print("car started")
#     @staticmethod
#     def pouse ():
#         print("car is pouse..")
        
# class Toyotacar (car):
#         def __init__ (self,name):
#             self.name = name
            
# class fortunar (Toyotacar):
#     def __init__(self, type):
#          self.type = type

# car1 = fortunar("diesel")
# car1.start()
 
 
 
#multiple inherite karva matte *****
class A :
    vara = ("welcome class A")
class B:
    varb =("welcome class B")
class c (A,B):
    varc = ("welcome class c")
c1 =  (c)
print(c1.varc)
print(c1.varb)
print(c1.vara)



#super key word ****


class car():
    def __init__(self,type):
         self.type = type
    @staticmethod
    def start ():
        print("car started")
    @staticmethod
    def pouse ():
        print("car is pouse..")
        
class Toyotacar (car):
        def __init__ (self,name,type):
            super().__init__(type)
            super().start()#*******
            self.name = name
            
car1 = Toyotacar("fortunar","electric")
print(car1.type)


# class na name ne badal va mate *********
class person():
    name = "harsh"
    @classmethod          #using class method ****
    def changename (cls ,name):
        cls.name = name
        
p1 = person()
p1.changename("ekta")
# print(p1.name)
print(person.name) 




#@proparty mate ****

class student:
    def __init__(self,phy,chem,math):
        self.physics = phy
        self.chem = chem
        self.math = math
    
    @property
    def persantage (self):
        return  str((self.physics + self.chem + self.math) /3) +"%"
    
stu1 = student (70,40,90)
print(stu1.persantage)    
stu1.physics = 50
print(stu1.persantage)



