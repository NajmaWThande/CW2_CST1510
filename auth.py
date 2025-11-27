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
        

