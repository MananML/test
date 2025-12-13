import random
import time

GUESS= 0
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def get_user_input():
    while True:
        top_range = input(f"{CLEAR_AND_RETURN}Input a number to get in that range: ")
        
        if top_range.isdigit():
            top_range = int(top_range)
            return top_range    
        else:
            print("Please kindly input a digit.")

def computers_guess(top_range):
    number = random.randint(0, top_range)
    return number

def check_value(number):
    global GUESS
    while True:
        guess = input("\033[31mMake a guess: ")
        GUESS += 1
        print("\033[0m", end="")
        if guess.isdigit():
            guess = int(guess)            
            if guess == number:
                print("You guessed right.")
                _ = input("Dou you want to play again (y or n)? ")
                if _.lower() == "y":
                    continue
                else:
                    quit()
            else:
                if guess < number:
                    print("Your guess is less than the required number.")
                else:
                    print("Your guess is greater than the required number.")
                
                break
        else:
            print("Please kindly input a digit.")
            break

def main():
    print(CLEAR)
    top_range = get_user_input()
    number = computers_guess(top_range)
    while True:
        check_value(number)

if __name__ == "__main__":
    main()