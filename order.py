from user import user

class order:
    def __init__(self, user, onumber): 
        self.user = user
        self.Onum = onumber

    def orderHistory(self):
        #write order history to file
        orders = open("orders.txt", "a")
        user_info = self.user.getInfo()
        for i in user_info:
            orders.write(str(i))
            orders.write(" ")
        
        orders.write(str(self.Onum))
        orders.write("\n")
        orders.close()

    def showHistory(self):
        orders = open("orders.txt", "r")
        print(orders.read())
        orders.close()