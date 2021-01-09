#lesson_13__2

import functionsHW13 as f13

#create new DB for notebook
db = []

print("Hello this is NoteBook-4900")

while True:
    action = input("Enter command[press <help> to show all commands or if you know this notebook, input your action]: ")

    if action == 'help':
        print("Welcome to NoteBook-4900 version 2.3 !")
        print("press CREATE_USER - to create new user")
        print("press CREATE_U_NOTE - to create user note")
        print("press READ_ALL - to read all notes in notebook")
        print("press READ_ONE - to read all notes ONLY one user")
        print("press USERNAMES - to read all usernames in notepad")
        print("press DELETE_NOTE - to remove one note")
        print("press UPDATE - to update user note")
        print("press PASSWORD - adding or changing password")
        print("press EXIT to exit from notebook")
    elif action == "CREATE_USER":
        username = input("Input username: ")
        while True:
            psword = input("Input your password: ")
            check_psword = input("Input again your password: ")
            if psword == check_psword:
                print("Password for user ", username ," added success!")
                break
            else:
                print("passwords not equal! try again")
        f13.create_user(db, username, psword)

    elif action == "CREATE_U_NOTE":
        name = input("input username for adding note: ")
        note = input("Input note: ")

        #checking for right username and password
        if f13.create_users_note(db, name, note):
            print("Note successfull added!")
        else:
            print("Wrong username or password!")

    elif action == "READ_ALL":
        f13.read_total(db)

    elif action == "USERNAMES":
        f13.read_users(db)

    elif action == "PASSWORD":
        tmp_name = input("Enter username: ")

        if f13.password(db, tmp_name):
            print("Password was changing or adding successfully!")
        else:
            print("Error! wrong username or current password")
        
    elif action == "READ_ONE":
        read_name = input("Enter username: ")

        f13.read_one_user(db, read_name)

    elif action == "UPDATE":
        name = input("Enter username: ")
        ID_note = int(input("Enter ID of note: "))
        updated_note = input("Enter new note: ")

        if f13.update_user_note(db, name, ID_note, updated_note):
            print("Note with ID =", ID_note, "was updated succesfull!")
        else:
            print("something wrong - password or username!")

    elif action == "DELETE_NOTE":
        name = input("Enter username: ")
        ID_note = int(input("Enter ID of note: "))

        if f13.delete_note(db, name, ID_note):
            print("Note was deleted succesfull!")
        else:
            print("Wrong password or username!")
    
    elif action == "EXIT":
        print("Goodbye")
        break
