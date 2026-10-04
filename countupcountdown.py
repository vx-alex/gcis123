def count_down(number):
    total =0
    while number >=0:
        print(number)
        total = total + number
        number = number - 1
    return total

def count_up(number):
    total =0
    count =0

    while count <= number:
        print (count)
        total = total + count
        count= count+ 1
    return total
def main():
    number = int(input("enter your number: "))

    print(count_up(number))
    print(count_down(number))
main()

