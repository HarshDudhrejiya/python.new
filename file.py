# f = open("data.txt","r")   je file ma lakhelu che e print karava mate
# # data = f.read()
# line1 = f.readline()
# print(line1)
# # line2 = f.readline()
# # print(line2)
# # print(data)
# # print(type(data))
# f.close()

# f = open("data.txt","w")     #je file  ma lakhvu hoy e lakhva mate
# data = f.write("i want to learn python , 123")
# # f.close()


# f = open("data.txt","r+")     #over write karva mate
# data = f.write("yahoo!")
# f.close()


# with open ("data.txt","r") as f:
#     datta = f.read()
#     print(datta)
  
# @ data ne replace karva mate  

# with open ("data.txt","r") as f:
#     datta = f.read()
#     new_data = datta.replace("harsh","ekta")
# print(new_data)

# with open ("data.txt","w") as f:
#     f.write(new_data)
  
# with open ("data.txt","r") as f:
#     datta = f.read()
#     if(datta.find("ekta")):
#         print("found")
#     else:
#         print("not found")  
        
        
        
def check_for_line ():
    word = "harsh"
    data = True
    line_no = 1
    with open("data.txt","r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
                return 
            line_no +=1
        return -1        
        
check_for_line()
        
        
    
# packej ne instal karva mate athva add karva mate pip lakhvany jo na hoy  to
# import os
# os.remove("data.txt")   #file ne delete karva mate
