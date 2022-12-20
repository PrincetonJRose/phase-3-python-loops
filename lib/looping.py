#!/usr/bin/env python3

def happy_new_year():
    # code goes here
    countdown = 10
    while countdown >= 0:
        if not countdown == 0:
            print( countdown )
        else:
            print( "Happy New Year!" )
        countdown -= 1
    pass

def square_integers(int_list):
    # code goes here
    # return [*map( lambda n: n*n, int_list )]
    return [ n * n for n in int_list ]
    pass

def fizzbuzz():
    # code goes here
    number = 1
    while number <= 100:
        match number:
            case number if not number % 3 and not number % 5:
                print( 'FizzBuzz' )
            case number if not number % 3:
                print( 'Fizz' )
            case number if not number % 5:
                print( 'Buzz' )
            case number if number % 3 and number % 5:
                print( number )
        number += 1
    pass
