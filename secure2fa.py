import pyotp
import bcrypt
import json
import os
import time

USER_FILE = 'users.json'

# Load existing users or initialize storage
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def register():
    users = load_users()
    username = input("Choose a username: ")
    if username in users:
        print("Username already exists.")
        return
    password = input("Choose a password: ")
    hashed_pw = hash_password(password)
    secret = pyotp.random_base32()
    users[username] = {'password': hashed_pw, '2fa_secret': secret}
    save_users(users)
    print("\n Registration successful.")
    print(f" 2FA Secret (store in your Authenticator App): {secret}")

def login():
    users = load_users()
    username = input("Username: ")
    if username not in users:
        print("User not found.")
        return
    password = input("Password: ")
    if not verify_password(password, users[username]['password']):
        print(" Incorrect password.")
        return
    otp = input("Enter 2FA OTP: ")
    totp = pyotp.TOTP(users[username]['2fa_secret'])
    if totp.verify(otp):
        print(" Login successful.")
    else:
        print(" Invalid OTP.")

def menu():
    print("""
===================
  Secure2FA CLI
===================
1. Register
2. Login
3. Exit
""")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Choose option: ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid input.")
