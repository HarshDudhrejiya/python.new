marks = [11.2 , 25.3 , 33.3 , 99.3 , 45.8]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

# list ma char , float , int badhi value ak sathe lakhi akvi
student = ["harsh" , 20.3 , "godhavadar"] 
print(student[0])
# list ni undar koi bhui name ne chnage karva mate
print(student)
student[0] = "ekta"   
print(student)

# list slicing mate 
print(marks[1:4])
print(marks[-3:-1])



# some list function
list = [1,3,2,4,7,5]
# 1) add karva mate
# list.append(6)
# print(list)

# 2) badhu line ma gothava mate
# list.sort()
# print(list) 

#list ma lakhelu undhu lakhva mate ama je sort karu hou  temj hoy
# list.sort(reverse=True)  
# print(list)

# 3) list ma lakhelu undhu lakhva mate
# list.reverse()
# print(list)

# 4) list ma insert add karva mate vache 
# list.insert(1, 5)
# print(list)

# 5) value ne vache thi delete or pop karva mate 
list.pop(3)
print(list)