from cart import cart
from order import order
from user import user 
from database import *
from item import item

#Notes about program
#Forgot about showing stock quantity to user code became to big and complex to implement later
#this means that stock is not shown between purchases
#we were confused on wheter or not payment address information was stored between executions
#of the program or just different purchases made during the same execution of the proram
#we went with the latter

#Further Documentation
#The user currently has to type the item they want to remove
#adding and removing is done one at a time
#because stock was not exposed to the user, neither was quantity
#so removing an item only removes the first one.
#a warning is printed before doing so


#Read in username and password from user
username = input("Enter your username: ")
password = input("Enter your password: ")

#order number
oNum = 0
total = 0
items = []

#create shopping cart
scart = cart()

#forward the username and password to login function which should check the database
login(username, password)

#create user
customer = user(username, password)

loop_flag = True

#start infinite loop 
while (loop_flag):
    #ask user to select a category
    print("Categories")
    print("1. for Household items")
    print("2. for Books")
    print("3. for Toys")
    print("4. for Small Electronics")
    print("5. to Show Cart")
    print("6. Remove from Cart")
    print("7. Finalize order")
    print("8. Show Order History")
    print("9. Logout")
    answer = str(input("Pick a Category 1-4 to add to cart or 5-7 for cart operations: "))

    #verify category
    if (answer == "1"):
        #ask what item they want
        print("---Items for Sale---")
        print("1. aluminum foil")
        print("2. toothpaste")
        print("3. salt")
        print("4. pepper")
        selection = str(input("Pick an item 1-4: "))

        #append to cart
        if (selection == "1"):
            #temporary item used to get price of an item
            stuff = item("aluminum foil")
            if (scart.addItem(stuff) == False):
                print("Sorry we are all out of that item at the moment")

        elif (selection == "2"):
            #temporary item used to get price of an item
            stuff = item("toothpaste")
            if (scart.addItem(stuff) == False):
                print("Sorry we are all out of that item at the moment")

        elif (selection == "3"):
            #temporary item used to get price of an item
            stuff = item("salt")
            if (scart.addItem(stuff) == False):
                print("Sorry we are all out of that item at the moment")

        elif (selection == "4"):
            #temporary item used to get price of an item
            stuff = item("pepper")
            if (scart.addItem(stuff) == False):
                print("Sorry we are all out of that item at the moment")


    elif (answer == "2"):
        #ask what item they want
        print("---Items for Sale---")
        print("1. Harry Potter Book")
        print("2. SW Design Book")
        print("3. Spiderman Book")
        print("4. Diary of a Wimpy Kid Book")
        selection = str(input("Pick an item 1-4: "))

        #append to cart
        if (selection == "1"):
            #temporary item used to get price of an item
            stuff = item("Harry Potter Book")
            if (scart.addItem(stuff) == False):
                print("Sorry we are all out of that item at the moment")

        elif (selection == "2"):
            #temporary item used to get price of an item
            stuff = item("SW Design Book")
            if (scart.addItem(stuff) == False):
                print("Sorry we are all out of that item at the moment")

        elif (selection == "3"):
            #temporary item used to get price of an item
            stuff = item("Spiderman Book")
            if (scart.addItem(stuff) == False):
                print("Sorry we are all out of that item at the moment")

        elif (selection == "4"):
            #temporary item used to get price of an item
            stuff = item("Diary of a Wimpy Kid Book")
            if (scart.addItem(stuff) == False):
                print("Sorry we are all out of that item at the moment")

    elif (answer == "3"):
        #ask what item they want
        print("---Items for Sale---")
        print("1. Spiderman Figure")
        print("2. Superman Figure")
        print("3. Pikachu Plushy")
        print("4. Charizard Card")
        selection = str(input("Pick an item 1-4: "))

        #append to cart
        if (selection == "1"):
            #temporary item used to get price of an item
            stuff = item("Spiderman Figure")
            if (scart.addItem(stuff) == False):
                print("Sorry we are all out of that item at the moment")

        elif (selection == "2"):
            #temporary item used to get price of an item
            stuff = item("Superman Figure")
            if (scart.addItem(stuff) == False):
                print("Sorry we are all out of that item at the moment")

        elif (selection == "3"):
            #temporary item used to get price of an item
            stuff = item("Pikachu Plushy")
            if (scart.addItem(stuff) == False):
                print("Sorry we are all out of that item at the moment")

        elif (selection == "4"):
            #temporary item used to get price of an item
            stuff = item("Charizard Card")
            if (scart.addItem(stuff) == False):
                print("Sorry we are all out of that item at the moment")

    elif (answer == "4"):
        #ask what item they want
        print("---Items for Sale---")
        print("1. Phone")
        print("2. Camera")
        print("3. Tablet")
        print("4. Laptop")
        selection = str(input("Pick an item 1-4: "))

        #append to cart
        if (selection == "1"):
            #temporary item used to get price of an item
            stuff = item("Phone")
            if (scart.addItem(stuff) == False):
                print("Sorry we are all out of that item at the moment")

        elif (selection == "2"):
            #temporary item used to get price of an item
            stuff = item("Camera")
            if (scart.addItem(stuff) == False):
                print("Sorry we are all out of that item at the moment")

        elif (selection == "3"):
            #temporary item used to get price of an item
            stuff = item("Tablet")
            if (scart.addItem(stuff) == False):
                print("Sorry we are all out of that item at the moment")

        elif (selection == "4"):
            #temporary item used to get price of an item
            stuff = item("Laptop")
            if (scart.addItem(stuff) == False):
                print("Sorry we are all out of that item at the moment")

    #print contents of the cart along with total
    elif (answer == "5"):
        scart.showCart()

    elif (answer == "6"):
        scart.showCart()
        print("Note: if the item appears twice. Only the first one will be removed.")
        removal = str(input("Type the whole name of the item to be removed: "))
        scart.rmItem(removal)
        scart.showCart()

    elif (answer == "7"):
        #create order
        oNum += 1
        total = scart.getTotal()
        items = scart.getItems()
        while (True):
            #have them enter in their address if they have
            if ((customer.getAddress() == "") or (customer.getPayment() == "")):
                customer.setAddress(str(input("Enter your address: ")))
             
                #have them enter in their payment if they haven't already
                if (customer.setPayment(str(input("Enter your credit card number: ")))):
                        print("---Confirm Purchase---")
                        confirmPurchase = str(input("Type yes to confirm otherwise type no: "))

                        #make the customer confirm their purchase
                        if confirmPurchase == "yes":
                            purchase = order(customer,total, items, oNum)
                            purchase.orderHistory()
                            scart.emptyCart()
                        else:
                            oNum -= 1
                        break
            
            else:
                #make the customer confirm their purchase
                print("---Confirm Purchase---")
                confirmPurchase = str(input("Type yes to confirm otherwise type no: "))

                if confirmPurchase == "yes":
                    purchase = order(customer, total, items, oNum)
                    purchase.orderHistory()
                    scart.emptyCart()

                else:
                    oNum -= 1
                    
                break
        

    elif (answer == "8"):
        #do stuff
        tmpOrder = order(None, total, items, oNum)
        tmpOrder.showHistory()

    elif (answer == "9"):
        #logout
        print("Thanks for shopping with us")
        quit()