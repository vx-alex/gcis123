while True:
    char = input("Enter a character (or \"exit\" to quit): ")
    if char.lower() == "exit":
        break
    code = ord(char)
    print("ASCII code:", code)
    
