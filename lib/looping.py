#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
    pass

def square_integers(int_list):
    squares = [integer ** 2 for integer in int_list]
    return(squares)
    # code goes here!
    pass

def fizzbuzz():
    # code goes here!
    i = 1
    while i <= 100:
        if i % 15 == 0:
            print("FizzBuzz")
            i += 1
        elif i % 3 == 0:
            print("Fizz")
            i += 1
        elif i % 5 == 0:
            print("Buzz")
            i += 1
        else:
            print(i)
            i += 1
    pass
