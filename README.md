# Week 7: Secure Authentication System
**Course:** CST1510 — Multi-Domain Intelligence Platform  
**Student Name:** Najma Thande  
**Student Number:** M01049398 

---

## **Project Overview**
This project implements a **secure user authentication system** in Python. Users can **register** and **login** using a username and password. Passwords are **hashed using bcrypt** for security, preventing plain-text storage.

---

## **Features**
- Register a new user with a username and password
- Secure password storage using bcrypt hashing
- User login verification
- Input validation for username and password
- Simple and clear command-line interface

---

## **Requirements**
- Python 3.x
- `bcrypt` library

Install the required library using:

```bash
pip install bcrypt

Project Structure
CW2_M0123456_CST1510/
│
├─ auth.py          # Main authentication program
├─ users.txt        # Stores registered users and hashed passwords
├─ README.md        # Project documentation
├─ requirements.txt # Project dependencies
└─ .gitignore       # Ignored files for Git

Run the Program
python auth.py

hoose an option from the menu:

1: Register a new user

2: Login

3: Exit

Follow the prompts to enter a username and password.


