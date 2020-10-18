class user:
    #attributes I think every user needs
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.address = ""
        self.creditcard = ""

    #this function should be called when the user is prompted for an address
    def setAddress(self, address):
        self.address = address

    #this function should be called when the user is prompted for his credit card
    #I still need to add some error checking as per the assignment instructions
    def setPayment(self, payment):
        try:
            if len(payment) == "10":
                self.creditcard = int(payment)
                return True
            else:
                return False
        except ValueError as ex:
            print("Invalid Characters in Credit Card")
            return False

    def getInfo(self):
        info = [self.username, self. address, self.creditcard]
        return info