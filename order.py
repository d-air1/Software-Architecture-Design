from user import user

class order:
    #constructure
    def __init__(self, user, total, items, onumber): 
        self.user = user
        self.total = total
        self.items = items
        self.Onum = onumber

    def orderHistory(self):
        #write order history to file
        orders = open("orders.txt", "a")
        user_info = self.user.getInfo()
        for i in user_info:
            orders.write(str(i))
            orders.write("\n")
        for i in self.items:
            orders.write(str(i))
            orders.write("\n")
        
        orders.write("Order Number: ")
        orders.write(str(self.Onum))
        orders.write("\n")
        orders.close()

    def showHistory(self):
        #opens list of orders and prints
        orders = open("orders.txt", "r")
        print(orders.read())
        orders.close()