#password generator.py

#Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

pw1 = []
pw2 = []
pw3 = []
final_password = []

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#pw.append(random.choices(letters, k=nr_letters))


while len(pw1) < nr_letters:
    pw1.append(random.choice(letters))

while len(pw2) < nr_symbols:
    pw2.append(random.choice(symbols))

while len(pw3) < nr_numbers:
    pw3.append(random.choice(numbers))



final_password.extend(pw1)
final_password.extend(pw2)
final_password.extend(pw3)


print(pw1)
print(pw2)
print(pw3)
print(final_password)
random.shuffle(final_password)


print(*final_password, sep = "")
