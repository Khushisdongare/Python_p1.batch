# Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Arithmetic operations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2

# Division and remainder
if num2 != 0:
    division = num1 / num2
    remainder = num1 % num2
else:
    division = "Undefined (division by zero)"
    remainder = "Undefined (modulo by zero)"

# Output arithmetic results
print("\nArithmetic Operations:")
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)

# Comparison
print("\nComparison Result:")
if num1 > num2:
    print("The first number is greater than the second.")
elif num1 < num2:
    print("The second number is greater than the first.")
else:
    print("Both numbers are equal.")
