#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

num = int(input("entern num"))
n1 = int("%s" % num)
n2 = int("%s%s" %(num,num))
n3 = int("%s%s%s" %(num,num,num))

print(n1+n2+n3)