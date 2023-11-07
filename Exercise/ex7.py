import random

def main():
    randomNum = random.randint(1, 100)
    if randomNum < 10:
        print(f'{randomNum}: You lose.')
    elif randomNum >= 10 and randomNum < 50:
        print(f'{randomNum}: Try again.')
    else:
        print(f'{randomNum}: You win!')


if __name__ == "__main__":
    main()


# random 1 - 100
# x < 10 "you lose"
# 10 < x < 50 "try again"
# x > 50 "you win"