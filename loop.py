# i = 1
# while i <=5:
#     print("harsh dudharejiya")
#     i+=1
    
# 1) print number from 1 to 100

# i = 1
# while i<=100:
#         print(i)
#         i+=1

# 2) print number from 100 to 1

# i = 100
# while i >= 1:   #stoping condition
#     print(i)
#     i-=1

# 3) print multiplication table
# n = int(input("enter number:")) 
# i = 1
# while i <= 10:
#     print(n*i)
#     i+=1


# 4) print the element of the following list using a loop;
# num = [1,4,9,16,25,36,49,64,81,100]
# idx = 0   # initiolization
# while  idx < len(num):
#     print(num[idx])
#     idx +=1
    
# 5) search for a number x in this tupal using loop
num = [1,4,9,16,25,36,49,64,81,100]
x = int(input("enter your number:"))
i = 0
while i < len(num):
  if num[i] == x:
    print("found number",i)  #i--> lakhvathi ketla number upar che e print thay jyare x --> lakhathi kyo number che e print thay 
    break

  i += 1
else:
      print("Number not found")
  

