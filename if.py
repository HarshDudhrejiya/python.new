# name = input("enter your light :")

# light = "green"
# light = "red"
# light = "yellow"
# if(name == "green"):
#     print("go",name)
# elif(name == "red"):
#     print("stop",name)
# elif(name == "yellow"):
#     print("start your car",name)
# else:
#     print("light is not working")
    
# Example: classify a number
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
elif num < 0:
    print("Negative")
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Zero")
