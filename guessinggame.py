def guessing_game():
    number = input("Pick a number: ")
    number = int(number)

    if number < 1 or number > 10:
        raise ValueError("Invalid guess!")

    print("You picked:", number)
guessing_game()

    