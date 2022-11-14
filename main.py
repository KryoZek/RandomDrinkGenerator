#!/usr/bin/python3
import random as rd
import sys



def main():

    setFlag = False

    if len(sys.argv)-1 == 1:
        drink_amount = int(sys.argv[1]) - 1
        setFlag = True

    drinks = []
    toppings = []

    with open("/home/kryozek/Reliquary/Codebase/Projects/RandDrinkGen/drinks.txt", 'r') as f:
        drinks = [line.rstrip() for line in f]

    f.close()

    with open("/home/kryozek/Reliquary/Codebase/Projects/RandDrinkGen/toppings.txt", 'r') as f:
        toppings = [line.rstrip() for line in f]

    f.close()

    ctr = 0
    while len(drinks) > 0:
        randDrink   =   drinks.pop(rd.randrange(len(drinks)))
        randTopping =   rd.choice(toppings)

        drink = randDrink + "\nTopping: " + randTopping
        ctr += 1

        print(f"\nDrink #{ctr}\n{drink}")

        if setFlag:
            if ctr > drink_amount:
                break
    print("\n")

main()
