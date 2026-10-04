def print_range(a_range):
    i = 0

    while i < len(a_range):
        print(a_range[i], end=" ")
        i += 1

    print()


print_range(range(0, 11))
print_range(range(0, 21, 2))
print_range(range(5, 16, 2))
print_range(range(10, -1, -1))
print_range(range(1,11,2))
print_range(range(5,51,5))
for i in range(1, 6):
    print(i * i)
total = 0

for i in range(0, 11, 2):
    total += i

print(total)

for i in range(1,6):
    print(">"*i)

for i in range(1,5):
    print("@" *(i-1) + "*" + "@" * (4-i))

text= "the midterm is on october 8th"
tokens = text.split()
print(tokens)
   
