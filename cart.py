from inventory import inventory
from item import item

class cart:
    #the main thing here is that I wanted the shopping cart to keep track of the items in the cart by appending to a list of item objects so first we need to import the item class I drafted up
    def __init__(self):
        self.total = 0
        self.items = []
        self.itemNum = 0
        self.inv = inventory()
    
    def getTotal(self):
        return self.total

    #this should append the added item to the list
    # I was thinking about returning the index of the item added for use with the remove function but was undecided at the time
    def addItem(self, item):
        #make sure stock isn't empty
        if (self.inv.get_stock(item.get_name()) <= 0):
            return False
        else:
            #add item to items array
            self.items.append(item)

            #update total
            self.total += item.get_price(item.get_name())

            #update inventory
            self.inv.rm_stock(item.get_name())
            return True

    #this should remove the iem from the lsit
    def rmItem(self, name):
        #rm item from items array
        tmp = ""
        if not self.items:
            for i in self.items:
                if (name.lower() == i.get_name().lower()):
                    #save name of item
                    tmp = i
                    #remove item
                    self.items.remove(i)
                    #update total
                    self.total -= item.get_price(tmp)
                    break
        else:
            print("Item not in cart or check spelling.")
    
    def showCart(self):
        print("---Items currently in your cart---")
        if not self.items:
            print("Cart is empty")
        
        else:
            for i in self.items:
                print(i.get_name() + " $" + str(i.get_price(i.get_name())))
                print("Total is $" + str(self.total))
                print()

    def emptyCart():
        if not self.items:
            return True
        else:
            return False