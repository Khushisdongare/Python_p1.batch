# Global variable
counter = 0

# Function to increment and print counter
def increment():
    global counter  # Declare that we're using the global 'counter'
    counter += 1
    print("Counter value:", counter)

# Call the function three times
increment()  # Output: 1
increment()  # Output: 2
increment()  # Output: 3
