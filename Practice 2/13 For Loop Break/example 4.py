# Using for loop to find invalid characters in password
password = "Cool password"
valid = "1234567890-=_+QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm.()!@#$%^&*"
for i in password:
    if i not in valid:
        print(f"Invalid password: should not contain character {i}")
        break
else:
    print("Valid password")
