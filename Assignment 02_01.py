# Guessing Game
# CS/2017/005
# W.T Dilshan


import random   # To import random number
x = random.randint(1, 100)  # x -> random number

i = 0
prev_n = n = 0   # n -> guess number and  prev_n -> previous guess number
check = False    # check -> boolean check

while True:
    check = False
    try:
        prev_n = n
        n = int(input("* Enter your guess number:"))
        if n < 1 or n > 100:        # check the guess is in the bound
            print("OUT OF BOUNDS !")
            print("You should enter numbers within the 1 to 100 ")
            check = True

    except:
        print("that's not a number!")   # when not input a number, executed this block
        continue

    if n == x:
        print("\nYour are guessed correctly.")
        print("*****YOU ARE WIN !! *****")
        break
        i = i + 1

    else:
        guess_gap = abs(x - n)  # get the absolute value between random value and guess the value

        if not check:
            if guess_gap <= 10:
                if not prev_n or abs(prev_n - x) > 10:
                    print("WARM!")
                elif guess_gap < abs(prev_n - x):
                    print("WARMER!")
                else:
                    print("COLDER!")

            elif guess_gap > 10:

                print("COLD!")

        i = i + 1

print("\nTotal no of guesses :", i+1)
