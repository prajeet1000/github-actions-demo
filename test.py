# This is a sample Python file

# Function to calculate the sum of two numbers
def add_numbers(a, b):
    return a + b

# Function to calculate the product of two numbers
def multiply_numbers(a, b):
    return a * b

# Main function
def main():
    # Get input from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    
    sum_result = add_numbers(num1, num2)
    product_result = multiply_numbers(num1, num2)

    # Print the results
    print("The sum of", num1, "and", num2, "is:", sum_result)
    print("The product of", num1, "and", num2, "is:", product_result)

# Call the main function
main()
