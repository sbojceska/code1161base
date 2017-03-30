"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""
from __future__ import division
from __future__ import print_function
from exercise1 import not_number_rejector
from exercise1 import super_asker
import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("Goood day,let's play")
    print("Enter a lowerBound:")
    lowerBound = not_number_rejector("your lower bound is:")
    upperBound = not_number_rejector("What is your upper bound?:")
    while upperBound <= lowerBound:
        print("re-enter upperBound")
        pass
    upperBound = int(upperBound)
    lowerBound = int(lowerBound)

    actualNumber = random.randint(lowerBound, upperBound)
    guess = False

    while not guess:
        try:
            input_number = int(raw_input("Guess Number:"))
            print("{} is valid".format(input_number))
            if input_number == actualNumber:
                print("{} is correct".format(input_number))
                guess = True
            elif input_number < actualNumber:
                print("too small. try again")
            elif input_number > upperBound:
                print("out of range")
            elif input_number < lowerBound:
                print("out of range")
            else:
                print("too big, try again")
        except Exception as e:
                print("Try again because it's not a number ({})".format(e))
        return "You got it!"
    pass

    actualNumber = random.randint(upperBound, lowerBound)
    guess = False

    while not guess:
        try:
            input_number = int(raw_input("Guess Number:"))
            print("{} is valid".format(input_number))
            if input_number == actualNumber:
                print("{} is correct".format(input_number))
            guess = True
            elif input_number < actualNumber:
                print("too small. try again")
            elif input_number > lowerBound:
                print("out of range")
            elif input_number < upperBound:
                print("out of range")
        else:
            print("too big, try again")
    except Exception as e:
            print("Try again because it's not a number ({})".format(e))
    return "You got it!"
    pass


if __name__ == "__main__":
    advancedGuessingGame()
