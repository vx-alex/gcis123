try:
     x_input = input("Enter x: ")
     y_input = input("Enter y: ")
     x = int(x_input)
     y = int(y_input)

     print("x / y =", (x/y))
except ValueError:
    print("Invalid number entered.")
except ArithmeticError:
    print("Can’t divide by 0.")
