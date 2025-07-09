# Step 1: Initial dictionary of students and grades
students = {
    "Alice": 88,
    "Bob": 75,
    "Charlie": 92
}

# Step 2: Function to add new students
def add_student(name, grade):
    students[name] = grade
    print(f"Added {name} with grade {grade}.")

# Add new students (you can repeat this part or replace it with user input)
add_student("Diana", 85)
add_student("Ethan", 90)

# Step 3: Calculate average grade
def calculate_average(grades_dict):
    if grades_dict:
        average = sum(grades_dict.values()) / len(grades_dict)
        return average
    return 0

average_grade = calculate_average(students)

# Step 4: Identify top performer
def top_performer(grades_dict):
    if grades_dict:
        top_name = max(grades_dict, key=grades_dict.get)
        return top_name, grades_dict[top_name]
    return None, 0

top_name, top_grade = top_performer(students)

# Step 5: Display results
print("\nStudent Grades:")
for name, grade in students.items():
    print(f"{name}: {grade}")

print(f"\nAverage Grade: {average_grade:.2f}")
print(f"Top Performer: {top_name} with grade {top_grade}")
