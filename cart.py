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
        for i in self.items:
            self.total += i.getPrice(i.getName())
        return self.total

    #this should append the added item to the list
    # I was thinking about returning the index of the item added for use with the remove function but was undecided at the time
    def additem(self, item):
        #add item to items array
        #update total
        #update item number

    #this should remove the iem from the lsit
    def rmitem(self, item):
        #rm item from items array
        #update total
        #update item number