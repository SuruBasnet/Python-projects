from calendar import c
import random

r = random.randrange(-6,12)

a = input("Enter your name: ")
print(f"Welcome {a} to Number guesser.In this game a random number is generated and you have to guess it, under 5 chances.If you guess the number at first try you get a lamborgundi.")

print("The number is between '-6' and '12'")

input("Press enter to play")

i = 5
def game():
    g = input("Guess the number: ")
    return g

g = int(game())

while i > 0:
    if g == r:
        print("YOU GOT IT! CONGRATS")
        quit()
    elif g != r:
        print(f"You still got {i} chances")
        g = int(game())
        i -= 1

    if i == 0:
        print("YOU LOSE")
        print(f"This was the number: {r}")
        quit()
 



