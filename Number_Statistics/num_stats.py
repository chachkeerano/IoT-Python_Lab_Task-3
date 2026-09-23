numbers = []

for i in range(10):
    n = float(input(f"Enter number {i+1}: "))
    numbers.append(n)

total = sum(numbers)
average = total / len(numbers)
largest = max(numbers)
smallest = min(numbers)

even_count = 0
odd_count = 0

for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\n--- Result ---")
print("Numbers entered:", numbers)
print("Sum:", total)
print("Average:", average)
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)