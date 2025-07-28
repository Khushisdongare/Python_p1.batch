class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}  # Dictionary to store course names and grades

    def enroll(self, course_name):
        if course_name not in self.courses:
            self.courses[course_name] = None
            print(f"{self.name} enrolled in {course_name}.")
        else:
            print(f"{self.name} is already enrolled in {course_name}.")

    def update_grade(self, course_name, grade):
        if course_name in self.courses:
            self.courses[course_name] = grade
            print(f"{self.name}'s grade updated for {course_name}: {grade}")
        else:
            print(f"{self.name} is not enrolled in {course_name}.")

    def calculate_gpa(self):
        valid_grades = [grade for grade in self.courses.values() if grade is not None]
        if not valid_grades:
            return 0.0
        return sum(valid_grades) / len(valid_grades)

    def display_info(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print("Courses and Grades:")
        for course, grade in self.courses.items():
            grade_display = grade if grade is not None else "Not graded"
            print(f"  - {course}: {grade_display}")
        print(f"GPA: {self.calculate_gpa():.2f}")
