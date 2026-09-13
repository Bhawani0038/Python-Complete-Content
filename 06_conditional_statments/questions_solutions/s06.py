"""Question: Determine the largest of three given numbers."""

first_number = 14
second_number = 9
third_number = 21

# Solution 1: compare with the built-in max function
print("Largest number:", max(first_number, second_number, third_number))




# Solution 2: compare each number with the other two
if first_number >= second_number and first_number >= third_number:
    largest = first_number
elif second_number >= first_number and second_number >= third_number:
    largest = second_number
else:
    largest = third_number
print("Largest number:", largest)