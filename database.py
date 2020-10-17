def login(username , password):
    #read in username and password from file
    db_file = open("users.txt", "r")
    db_text = str(db_file.readline())
    users = db_text.split(": ")

    #fix password
    password = password + "\n"

    #temporarily hardociding the user login until sqlite database is implemented
    if (username == users[0]) and (password == users[1]):
        print("Login Successful...")
        db_file.close()
        return True
    else:
        print("Login Failed: Wrong username or password")
        print("Terminating program due to failed login...")
        db_file.close()
        quit()
