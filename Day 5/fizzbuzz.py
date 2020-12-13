#fizzbuzz.py

for numbers in (range(1, 101)):
    if numbers % 15 == 0:
        print("fizzbuzz")
    elif numbers % 5 == 0:
        print("buzz")
    elif numbers % 3 == 0:
        print("fizz")
    else:
        print(numbers)

        
        

