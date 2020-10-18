class user:
    #Initializes variables that allows the user to login and purchase items
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.address = ""
        self.creditcard = ""

    #This function should be called when the user is prompted for an address
    def setAddress(self, address):
        self.address = address

    #This function is called when the user is prompted for a credit card
    def setPayment(self, payment):
        try:
            #Ensures that user enter credit number of the length of special OSC purchasing card
            if len(payment) == 10:
                self.creditcard = int(payment)
                return True
            else:
                print("Incorrect card format.")
                print("Please re-enter your information")
                print()
                return False
        except ValueError as ex:
            print("Invalid Characters in Credit Card")
            return False

    def getInfo(self):
        info = [self.username, self. address, self.creditcard]
        return info

    def getAddress(self):
        return self.address

    def getPayment(self):
        return self.creditcard