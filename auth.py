import bcrypt
import os

# function to hash password

def hash_password(plain_password):
    password_bytes = plain_password.encode()

    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(password_bytes, salt)

    return hashed.decode()