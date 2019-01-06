import random

def main():
    guess_correct = False
    random_min = 0
    random_max = 100

    while not guess_correct:
        guess = random.randint(random_min, random_max)
        print("My guess is " + str(guess))

        answer = input("Input 0 if the guess is too low, 1 if the guess is correct, 2 if the guess is too high, and q to quit\n")

        if answer == "0":
            random_min = guess + 1
        elif answer == "1":
            guess_correct = True
            print("My guess was correct!")
        elif answer == "2":
            random_max = guess - 1
        elif answer == "q":
            guess_correct = True
        else:
            print("Invalid input :/")

if __name__ == "__main__":
    main()
