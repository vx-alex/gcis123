def search_word(filename):
    word = input("Enter a Word to Search: ")
    f = open(filename, "r-")
    found = False
    for line in f.read().split():
        if line.strip() ==word:
            found = True
            break
    f.close()
    if found:
        print("Word Found")
    else:
        print("Word not Found")
search_word("input.txt")