# concatenation
str1 = ("harsh")
str2 = "dudharejiya"
len1 = (len(str1))

finallystr = str1 + " " + str2
print(finallystr)
print(len1)
print (str1[3])
print(str1[1:4])

# kya word jode end karavu che ana mate 

str = "dudharejiyaharsh@2005.com"
print(str.endswith("com"))   
# print(str.endswith("con"))  false


# pelo word capital karva mate
str = str.capitalize()
print(str)


# word ne replace karva mate 
print(str.replace("harsh" , "hasmukhbhai"))

# word no number gotva mate 
print(str.find("a"))

# ketlai var worde athava leter ave che e chek karva mate 
print(str.count("h"))

# bija function mate str . kari ne chhek kari levan 

name = input("Enter your name: ")
print( name.upper())
