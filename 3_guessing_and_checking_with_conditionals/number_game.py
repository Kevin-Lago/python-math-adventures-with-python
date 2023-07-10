from random import randint


def number_game() -> None:
    number = randint(1, 100)
    guess = get_guess()

    while guess:
        if number == guess:
            print(f"That's correct you guessed the number! {number}")
            break
        elif number > guess:
            print("Your guess is too low.")
        elif number < guess:
            print("Your guess is too high.")

        guess = get_guess()


def get_guess() -> int:
    while True:
        try:
            return int(input("Type in your guess"))
        except ValueError:
            print("Value must be an Integer")


if __name__ == '__main__':
    number_game()
