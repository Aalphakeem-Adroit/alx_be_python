size = int(input("Enter the size of the pattern: "))
tracker = 0

while tracker < size:
    for i in range(size):
        print("*", end="")
    print()
    tracker += 1