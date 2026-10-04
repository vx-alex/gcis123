name = input("enter a string: ")
print(name)
print(name[::-1])

if name == name[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

