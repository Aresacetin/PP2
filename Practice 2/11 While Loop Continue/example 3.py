# Password creation with validation
while True:
    password = input("Create a password (must be at least 6 chars): ")
    if len(password) < 6:
        print("Too short! Try again.")
        continue
    
    print("Password accepted!")
    break # Use break to exit once successful

