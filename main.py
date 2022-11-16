#!/usr/bin/python3
import random as rd
import sys


def main():

    with open("/home/kryozek/Reliquary/Codebase/Projects/RandDrinkGen/drinks.txt", 'r') as f:
        drinks = [line.rstrip() for line in f]
    f.close()

    with open("/home/kryozek/Reliquary/Codebase/Projects/RandDrinkGen/toppings.txt", 'r') as f:
        toppings = [line.rstrip() for line in f]
    f.close()

    drink_amount = len(drinks)

    if len(sys.argv)-1 == 1:
        drink_amount = int(sys.argv[1])

    for i in range(drink_amount):
        randDrink   =   drinks.pop(rd.randrange(len(drinks)))
        randTopping =   rd.choice(toppings)

        drink = randDrink + "\nTopping: " + randTopping
        print(f"\nDrink #{i+1}\n{drink}")

    print("\n")

main()