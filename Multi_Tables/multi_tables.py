n = int(input("Enter a number n: "))

for table in range(1, n + 1):
    for i in range(1, 11):
        print(f"{table} x {i} = {table * i}")
    print()