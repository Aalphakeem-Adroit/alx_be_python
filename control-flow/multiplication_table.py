number = input("Enter a number to see its multiplication table: ")

for num in range(1, 11):
    result = int(number) * num
    print(number, "*", num, "=", result)