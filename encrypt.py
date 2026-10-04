while True:
  def encrypt_letter(letter, shift):
    code = ord(letter)
    code = code + shift

    if letter.islower() and code > ord('z'):
        code = code - 26

    if letter.isupper() and code > ord('Z'):
        code = code - 26

    return chr(code)


  def main():
    letter = input("Enter a letter to encrypt: ")
    shift = 3
    encrypted_letter = encrypt_letter(letter, shift)
    print(f"The encrypted letter is: {encrypted_letter}")


  main()