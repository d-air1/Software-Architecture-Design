from cart import cart
from order import order
from user import user 
from database import *

#Read in username and password from user
username = input("Enter your username: ")
password = input("Enter your password: ")

#create shopping cart
scart = cart()

#forward the username and password to login function which should check the database
login(username, password)

loop_flag = True

#start infinite loop 
while (loop_flag):
    #ask user to select a category
    print("Categories")
    print("1. for Household items")
    print("2. for Books")
    print("3. for Toys")
    print("4. for Small Electronics")
    answer = str(input("Pick a Category 1-4: "))

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
            scart.addItem("aluminum foil")
        elif (selection == "2"):
            scart.addItem("toothpaste")
        elif (selection == "3"):
            scart.addItem("salt")
        elif (selection == "4"):
            scart.addItem("pepper")


    if (answer == "2"):
        #ask what item they want
        print("---Items for Sale---")
        print("1. Harry Potter Book")
        print("2. SW Design Book")
        print("3. Spiderman Book")
        print("4. Diary of a Wimpy Kid Book")
        selection = str(input("Pick an item 1-4: "))

        #append to cart
        if (selection == "1"):
            scart.addItem("Haryy Potter Book")
        elif (selection == "2"):
            scart.addItem("SW Design Book")
        elif (selection == "3"):
            scart.addItem("Spiderman Book")
        elif (selection == "Diary of a Wimpy Kid Book"):
            scart.addItem("pepper")

    if (answer == "3"):
        #ask what item they want
        print("---Items for Sale---")
        print("1. Spiderman Figure")
        print("2. Superman Figure")
        print("3. Pikachu Plushy)
        print("4. Charizard Card")
        selection = str(input("Pick an item 1-4: "))

        #append to cart
        if (selection == "1"):
            scart.addItem("Spiderman Figure")
        elif (selection == "2"):
            scart.addItem("Superman Figure")
        elif (selection == "3"):
            scart.addItem("Pikachu Plushy")
        elif (selection == "4"):
            scart.addItem("Charizard Card")

    if (answer == "4"):
        #ask what item they want
        print("---Items for Sale---")
        print("1. Phone")
        print("2. Camera")
        print("3. Tablet")
        print("4. Laptop")
        selection = str(input("Pick an item 1-4: "))

        #append to cart
        if (selection == "1"):
            scart.addItem("Phone")
        elif (selection == "2"):
            scart.addItem("Camera")
        elif (selection == "3"):
            scart.addItem("Tablet")
        elif (selection == "4"):
            scart.addItem("Laptop")