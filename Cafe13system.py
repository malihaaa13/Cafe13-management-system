import mysql.connector as mysql

db = mysql.connect(host="localhost", user="root", database="Cafe 13")
command_handler = db.cursor(buffered=True)

def admin_entry():
    print("Login successful!")

    while 1:
        print("\n\nAdmin Entry\n1. Register new Staff\n2. Register new Manager\n3.Delete existing Staff\n4. Delete existing Manager\n5. Logout")

        option_user = input("Option number: ")
        if option_user == "1":
            print("\n\nRegister New Staff")
            username = input("Staff username: ")
            password = input("Staff password: ")
            query_vals = (username, password)
            command_handler.execute("INSERT INTO users (username, password, privilege) VALUES (%s, %s, 'Staff')", query_vals)
            db.commit()
            print(username + " has been registered as a Staff")

        elif option_user == "2":
            print("\n\nRegister New Manager")
            username = input("Manager username: ")
            password = input("Manager password: ")
            query_vals = (username, password)
            command_handler.execute("INSERT INTO users (username, password, privilege) VALUES (%s, %s, 'Manager')",
                                    query_vals)
            db.commit()
            print(username + " has been registered as a Manager")

        elif option_user == "3":
            print("\n\nDelete Existing Staff Account")
            username = input("Staff username: ")
            query_vals = (username, "Staff")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User could not be found")
            else:
                print(username + " has been deleted!")

        elif option_user == "4":
            print("\n\nDelete Existing Manager Account")
            username = input("Manager username: ")
            query_vals = (username, "Manager")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User could not be found")
            else:
                print(username + " has been deleted!")

        elif option_user == "5":
            break

        else:
            print("No valid option selected!")

def admin_login():
    print("\n\nAdmin Login\n")
    username = input("Username: ")
    password = input("Password: ")
    if username == "Cafe13":
        if password == "MalihaAlam132000":
            admin_entry()
        else:
            print("INCORRECT PASSWORD!")
    else:
        print("Login information could not be recognised!")

def main():
    while 1:
        print("Welcome to the Cafe13 system!\n\n1. Login as Staff\n2. Login as Manager\n3.Login as Admin")

        option_user = input("Option number: ")
        if option_user == "1":
            print("Staff Login")
        elif option_user == "2":
            print("Manager Login")
        elif option_user == "3":
            admin_login()
        else:
            print("Invalid option")

main()




