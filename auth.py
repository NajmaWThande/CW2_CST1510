import bcrypt
import os

# function to hash password

def hash_password(plain_password):
    password_bytes = plain_password.encode()

    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(password_bytes, salt)

    return hashed.decode()

# this function is to verify the password during login

def verify_password(plain_password, hashed_password):
    password_bytes = plain_password.encode()
    hashed_bytes = hashed_password.encode()

    return bcrypt.checkpw(password_bytes, hashed_bytes)


def user_exists(username):
    if not os.path.exists("user.txt"):
        return False
    with open ("user.txt", "r") as file:
         for line in file:
            stored_username = line.strip().split(",")[0]
            if stored_username == username:
                return True
    return False
        
# register a new user

def register_user(username, password):
    if user_exists(username):
        print(f"Error: The username '{username}' is already taken.")
        return False
    
    hashed = hash_password(password)

    with open("user.txt", "a") as file:
        file.write(f"{username},{hashed}\n")

    print(f"Success: User '{username}' has been registered")
    return True

# the login function

def login_user(username, password):
    if not os.path.exists("user.txt"):
        print("Error: No users registered yet.")
        return False
    
    with open("users.txt","r") as file:
        for line in file:
            stored_username, stored_hash = line.strip().split(",")

            if stored_username == username:
                if verify_password(password, stored_hash):
                    print(f"Login successful. Hello there, {username}!")
                    return True
                else:
                    print("Error: Incorrect password")
                    return False
    
    print("Error: Username not found.")
    return False

# username validation

def validate_username(username):
    if len(username) < 3 or len(username) > 20:
        return False, "Username can only contain letters and numbers."
    
    return True, ""

# Password validation

def validate_password(password):
    if len(password) < 6:
        return False, "Password must be at least 6 characters long."
    
    return True, ""

# table on display

def display_menu():
    print("\n" + "=" * 50)
    print("  AUTHENTICATION SYSTEM  ")
    print("=" * 50)
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print("=" * 50)


# Main Program

def main():
    while True:
        display_menu()
        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "1":
            username = input("Enter a username: ").strip()
            valid, msg = validate_username(password)
            if not valid:
                print("Error:", msg)
                continue

            password = input("Enter a password please: ").strip()
            valid, msg = validate_password(password)
            if not valid:
                print("Error:", msg)
                continue

            register_user(username, password)

        elif choice == "2":
            username = input("Enter your usrname: ").strip
            password =  input("Enter your password: ").strip()
            