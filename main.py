import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

lenght = int(input("Введите длину паролья: "))

password = ""

for i in range(lenght):
    password += random.choice(symbols)

print(password)
