#homework_13
#functions

data_base = []  #[[['Andrew', 'password'], [list of Andrew's notes]], [....]]  - data structure in my notepad

#generating random password. For this program - generating password only for administrator!
import random

def random_password(length, letter = True, number = True, symbols = True):
    letter = 'abcdefghijABCDFJZXY'
    number = '0123456789'
    symbols = '!@#$%^&*()_+~'

    p = []
    for i in range(length):
        p.append(' ')
        
    for i in range(length):
        if random.randint(0, 2):
            p[random.randint(0, length - 1)] = letter[random.randint(0, len(letter) - 1)]
        elif random.randint(0, 2):
            p[random.randint(0, length - 1)] = number[random.randint(0, len(number) - 1)]
        elif random.randint(0, 2):
            p[random.randint(0, length - 1)] = symbols[random.randint(0, len(symbols) - 1)]

    pswd = ''
    for elem in p:
        pswd += elem
        
    return pswd

password_admin = random_password(18)
print("Current administrator password:", password_admin)

#create user + password
def create_user(data_base, name, password):
    #list for total data of user
    l = list()
    #list of user information only!
    user_info = [name]
    #password can not be equal! just a simple checking. but not so good.
    if password == name:
        print("Bad password!")
    else:
        user_info.insert(1, password)
    l.append(user_info)
    #create list for user notes
    l_notes = []
    l.append(l_notes)
    data_base.append(l)
    print(data_base)
    return name

#create user's note
def create_users_note(data_base, name, note):
    count_trying = 0
    for i in range(len(data_base)):
        if data_base[i][0][0] == name:
            while True:
                user_pass = input("Enter password: ")
                if count_trying > 3:
                    return False
                if user_pass == data_base[i][0][1]:
                    data_base[i][1].append(note)
                    return True
                else:
                    count_trying += 1
                    print("Wrong password! try again")
    return False

def password(DB, username):
    for i in range(len(DB)):
        if DB[i][0][0] == username:
            if len(DB[i][0]) == 1:
                add_pass = input("Enter your first password: ")
                DB[i][0].append(add_pass)
                return True
            else:
                check_current_pass = input("Enter your current password: ")
                if check_current_pass == DB[i][0][1]:
                    while True:
                        new_pass = input("Enter your new password: ")
                        repeat_pass = input("Repeat your new password: ")
                        if new_pass == repeat_pass:
                            DB[i][0][1] = new_pass
                            return True
                        else:
                            print("Inputing passwords is not equal! try again")
    return False

#read

#read usernames
def read_users(data_base):
    print("User ID\t\tUser Name")
    for i in range(len(data_base)):
        print("  ", i, "\t\t", data_base[i][0][0])

#read total information in Database. Only for administrator!
def read_total(DB):
    input_admin_pass = input("Enter Admin password: ")
    if password_admin == input_admin_pass:
        print("User ID\t\tUser Name\t\tPassword")
        for i in range(len(DB)):
            print("  ", i, "\t\t", DB[i][0][0], "\t\t", DB[i][0][1])
            print("Notes:")
            for j in range(len(DB[i][1])):
               print("Notes ID:", j, "||Note: ", end = "  ")
               print(DB[i][1][j])
            print("================")
    else:
        print("Error! Wrong password!")

#user operation - read information of yourself.
def read_one_user(DB, username):
    for i in range(len(DB)):
        if DB[i][0][0] == username:
            tmp_pass = input("Enter password: ")
            if tmp_pass == DB[i][0][1]:
                print("User ID\t\tUser Name\tPassword")
                print("  ", i, "\t\t", DB[i][0][0], "\t\t", DB[i][0][1])
                print("Notes:")
                for j in range(len(DB[i][1])):
                    print("Notes ID:", j, "||Note: ", end = "  ")
                    print(DB[i][1][j])
                break
            else:
                print("wrong password!")
                return False
    return False

#user operation - updating user notes
def update_user_note(DB, name, ID_note_change, new_note):
    for i in range(len(DB)):
        if DB[i][0][0] == name:
            user_pass = input("Enter your password: ")
            if DB[i][0][1] == user_pass:
                for j in range(len(DB[i][1])):
                    if j == ID_note_change:
                        DB[i][1][j] = new_note
                        return True
            else:
                print("Wrong password! try again")
    return False

def delete_note(DB, name, ID):
    for i in range(len(DB)):
        if DB[i][0][0] == name:
            user_pass = input("Enter your password: ")
            if DB[i][0][1] == user_pass:
                for j in range(len(DB[i][1])):
                    if j == ID:
                        DB[i][1].remove(DB[i][1][j])
                        return True
            else:
                print("Wrong password! try again")
    return False

