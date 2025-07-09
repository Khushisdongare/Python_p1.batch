# 1. Create a tuple of 5 student names
students = ("John", "Emma", "Michael", "Alice", "Sophia")

# 2. Print the second student's name (index 1)
print("Second student:", students[1])

# 3. Check if "Alice" is in the tuple
is_alice_present = "Alice" in students
print("Is Alice in the tuple?:", is_alice_present)

# 4. Concatenate with another tuple of 3 new students
new_students = ("David", "Olivia", "Liam")
all_students = students + new_students

# 5. Print the length of the final tuple
print("All students:", all_students)
print("Total number of students:", len(all_students))
