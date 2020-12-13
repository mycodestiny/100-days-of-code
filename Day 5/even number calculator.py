# even number calculator.py
numbers = list(range(1, 101))

sum = 0

for number in numbers:
    if number % 2 == 0:
        sum += number

print('the total of all the even numbers is: ', sum)

odd_sum = 0

for number in numbers:
    if number % 2 != 0:
        odd_sum += number

print('the total of all the odd numbers is: ', sum)
