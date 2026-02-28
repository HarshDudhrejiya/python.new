# class car():
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
        
#     def start (self):
#         self.acc = True
#         self.clutch = True
#         self.brk = True
#         print("start the car")
# car1 = car()
# car1.start()


# 2)acoount se debit or credit 

class account():
    def __init__(self,bal,acc):
        self.blance = bal
        self.account = acc
        
    def debit (self,amount):
        self.blance -= amount
        print("rs..",amount ,"was debited")
        print("total balance :",self.get_balance())
    def credit (self,amount):
        self.blance += amount
        print("rs..",amount ,"was credited")
        print("total balance :",self.get_balance())
    def get_balance(self):
        return self.blance 

acc1 = account(10000,1234)
acc1.debit(2000)
acc1.credit(1000)
acc1.credit(20000)

        
        
