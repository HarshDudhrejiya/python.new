
#function bananva mate easy to way

# def calc_sum (a, b):  #a and b ne peramiter kevay
#     sum = a+b
#     print(sum)
#     return sum

# calc_sum (5,5)  #function call
# calc_sum (4,3)


#average of 3 num

# def calc_sum (a,b,c):
#     sum = a+b+c
#     print("the sum is:",sum)
#     avg = sum /3
#     print("the avg is",avg)
#     return avg

# calc_sum(1,2,3)

# 1) waf to print the length of a list (list is the parameter)
# cities = ["gujrat","pune","surat","ahm","amreli"]
# star = ["ironman","spaidar man","thor","mogenbo"]

# def calc_len (list):
#     print(len(list))
    
# calc_len(cities)
# calc_len(star)

# 2) waf to print the element of list in a single line.(list is the parameter)

# cities = ["gujrat","pune","surat","ahm","amreli"]
# star = ["ironman","spaidar man","thor","mogenbo"]

# def calc_line (list):
#     print(list)
    
# calc_line(star)
# calc_line(cities)

# 2 or) upar na question ne biji rite lakhva mate jema string  na coma nai ave
# cities = ["gujrat","pune","surat","ahm","amreli"]
# star = ["ironman","spaidar man","thor","mogenbo"]
 
# def print_len (list):
#     print(len(list))
    
# def print_list (list):
#     for item in list :
#         print(item , end="")
        
        
# print_list(cities)
# print_list(star)

# 3) waf to the factorial  of n (n is the parameter)
# def cal_fact (n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#         print(fact)
        
# cal_fact(5)


# 4) to convert usd to inr

def converter (usd_val):
    inr_val  = usd_val * 83
    print(usd_val, "USD =", inr_val,"INR")
    
converter(2)