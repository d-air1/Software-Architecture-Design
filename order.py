from user import user

class order:
    oNum = 0
    def __init__(self, user): 
        self.user = user
        if self.user != None:
            order.Onum += 1

    def orderHistory(self):
        #write order history to file
        orders = open("orders.txt", "a")
        user_info = self.user.getInfo()
        for i in user_info:
            orders.write(i)
            orders.write(" ")
        
        orders.write(order.Onum)
        orders.write("\n")
        orders.close()

    def showHistory(self):
        orders = open("orders.txt", "r")
        print(orders.read())
        orders.close()