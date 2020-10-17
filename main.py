from cart import cart
from item import item
from inventory import inventory
from order import order
from user import user 
from database import *

#Read in username and password from user
username = input("Enter your username: ")
password = input("Enter your password: ")

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
        #append to cart
        #update inventory

    if (answer == "2"):
        #ask what item they want
        #append to cart
        #update inventory