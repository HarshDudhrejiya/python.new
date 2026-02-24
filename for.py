# tup = (1,2,3,4,5,6,7,8,9)   #list,tupel, string game te lakhishkiye

# for val in tup:
#     print(val)
    
    
# 1) print the element of the following list using a loop:
list = [1,4,9,16,25,36,49,64,81,100]
for val in list:
    print(val)
    
# 2) search for a number x in this tupel using loop:
tup = (1,4,9,16,25,36,49,64,81,100,36)    #linear search kevay
x = 36
idx = 0

for val in tup:
    
    if(val == x):
    
        print("number is found at idx",idx)
        
        break    #jo break na hot to 5 and 10 ans avat
    idx +=1
    # print(val)