def sum_of_odds():
    total = 0

    while True:
        number = int(input("Enter a number: "))

        if number == 0:
            break

        if number % 2 == 0:
            continue

        total = total + number

    return total


def main():
    result = sum_of_odds()
    print("Sum =", result)


main()