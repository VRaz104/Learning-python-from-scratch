import random
import string
Password_length=int(input("How long do you want your password to be:"))
Characters=string.ascii_letters
Characters+=string.digits
Characters+=string.punctuation
Password=""
for i in range(Password_length):
    Password+=random.choice(Characters)
print("Your password is:", Password)