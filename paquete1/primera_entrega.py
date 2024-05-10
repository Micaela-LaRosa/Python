# Database to store usernames and passwords
database = {}

# Function to register users and passwords
def register_user(database):
    option = ''
    while True:
        user_message = "Enter a username (or type 'exit' to return to the main menu): "
        password_message = "Enter a password (or type 'exit' to return to the main menu): "
        username = input(user_message)
        if username.lower() == 'exit':
            break
        elif username == '':
            print("You must register a username or type 'exit' to return to the main menu.")
            continue
        password = input(password_message)
        if password.lower() == 'exit':
            break
        elif password == '':
            while True:  # Loop to give the option to enter a new password
                option = input("You must enter a value for the password. Do you want to enter the password again? (s/n): ")
                if option.lower() == 's':
                    password = input("Enter a password: ")
                    if password.lower() == 'exit':
                        break
                    elif password == '':
                        print("You must enter a value for the password.")
                        continue
                    else:
                        break
                elif option.lower() == 'n':
                    break  # Exit the loop to enter another username or return to the main menu
                else:
                    print("Invalid option.")
                    continue
        if option.lower() == 'n':
            continue  # Request another username
        database[username] = password
        if password.lower() != 'exit':
            print("User registered successfully.")


# Function to display information of registered users
def show_users(database):
    if not database:
        print("No users registered.")
    else:
        print("Registered users:")
        for username, password in database.items():
            print(f"Username: {username}, Password: {password}")


# Function for user login
def login(database):
    while True:
        username = input("Enter your username (or type 'exit' to return to the main menu): ")
        if username.lower() == 'exit':
            return
        if username in database:
            while True:
                password = input("Enter your password (or type 'exit' to return to the main menu): ")
                if password.lower() == 'exit':
                    return
                if database[username] == password:
                    print("Login successful.")
                    return
                else:
                    print("Incorrect password. Please try again.")
        else:
            print("Username not registered. Please try again.")


# Main menu
while True:
    print("\n1. Register user")
    print("2. Show registered users")
    print("3. Login")
    print("4. Exit")
    option = input("Select an option: ")

    if option == '1':
        register_user(database)
    elif option == '2':
        show_users(database)
    elif option == '3':
        login(database)
    elif option == '4':
        print("Exiting the program...")
        break
    else:
        print("Invalid option. Please select a valid option.")
