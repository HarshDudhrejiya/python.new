# def show (n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)
    
# show(5)


 #factorial mate 
def fact (n):
    if (n==1 or n==0):
        return 1
    return n * fact (n - 1)
print (fact(3) )   


#write  a recursiv fun to calculat the sum of first n natural num 
def calc_sum (n):
    if (n == 0):
        return 0
    return(calc_sum (n-1) + n)

sum = calc_sum(10)
print(sum)

#write a recursiv fun to print all element in list
def print_list (list, idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

frut = ["mango","banana","apple","graps"]
print_list(frut)
    
    