#Code that checks if your password is strong enough

import string
password=str(input("Your password is:"))
uppercase=False
lowercase=False
digits=False
symbols_bool=False
length=False
strong=False
symbols=string.punctuation


while strong==False:
    for char in password:
        if char.isupper():
           uppercase=True
    for char in password:
        if char.islower():
           lowercase=True
    for char in password:
        if char.isdigit():
           digits=True
    for char in password:
        if char in symbols:
            symbols_bool=True
    if len(password)>8:
        length=True
    if uppercase==False:
        print("Your password needs to contain uppercase letters!")
        print("\n")
    if lowercase==False:
        print("Your password needs to contain lowercase letters!")
        print("\n")
    if digits==False:
        print("Password must contain numbers!")
        print("\n")
    if symbols_bool==False:
        print("Password must contain symbols!")
        print("\n")
    if length==False:
        print("Password is too short!")
        print("\n")
    if uppercase==True and lowercase==True and digits==True and symbols_bool==True and length==True:
        print("Password is strong enough!")
        strong=True
        break
    password=str(input("Your password is:"))
    print("\n")