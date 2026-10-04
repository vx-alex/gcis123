def encryptletter(letter, shift):
    letter_code = ord(letter)
    shifted_code = letter_code + shift

    if letter_code <= ord('Z'):
        if shifted_code > ord('Z'):
            shifted_code -= 26

    else:
        if shifted_code > ord('z'):
            shifted_code -= 26

    shifted_letter = chr(shifted_code)
    return shifted_letter
print(encryptletter('A', 3))  # D
print(encryptletter('Z', 3))  # C
print(encryptletter('a', 3))  # d
print(encryptletter('z', 3))  # c