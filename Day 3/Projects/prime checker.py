
# This is to check whether or not a number is prime


def prime_checker(number):
    if number < 1:
        print('Please choose a number > 1')
    if type(number) != int:
        print('Please choose an integer')

    for i in range(0, number):
        if (number % 2) == 0:
            print('This is not a prime number')
            break
        else:
            print('This is a prime number')
        


prime_checker(5)


