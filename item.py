class item:
    #I was trying to dynamically set the attributes for the item class based off of the name passed to it
    def __init__(self, name):
        self.name = name

        #determine price based off of name, something along these lines
        #there should be a few more if statements here but first we need to come up with a list of items to sale
        if (name == ""):
            self.price = 5 

