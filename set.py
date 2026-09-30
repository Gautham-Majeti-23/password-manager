"""
Allows the user to make their own password to the corresponding service
"""
from storer import save_generated_password

# Taking the intended service and password from user
service = input("service name: ")
password = input("password: ")

# Storing to the database with function from storer.py
save_generated_password(service=service, password=password)
