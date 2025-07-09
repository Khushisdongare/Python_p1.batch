# 1. Combine first and last name
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# 2. Formatted string for item and price
item = "laptop"
price = 999.99
formatted_string = f"The price of {item} is ${price}"
print(formatted_string)

# 3. Convert "hello world" to uppercase
text = "hello world"
uppercase_text = text.upper()
print("Uppercase:", uppercase_text)

# 4. Use .join() to make a sentence
words = ['Python', 'is', 'awesome']
sentence = ' '.join(words)
print("Joined Sentence:", sentence)

# 5. Print today's date in "DD-MM-YYYY" format
from datetime import datetime
today = datetime.today()
formatted_date = today.strftime("%d-%m-%Y")
print("Today's Date:", formatted_date)
