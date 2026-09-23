marks = []

for i in range(5):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

total = sum(marks)
percentage = (total / 500) * 100

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

failed_subject = any(mark < 40 for mark in marks)
result = "Fail" if failed_subject else "Pass"

print("\n--- Result ---")
print("Marks entered:", marks)
print("Total marks:", total)
print("Percentage: {:.2f}%".format(percentage))
print("Grade:", grade)
print("Result:", result)