class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}       # {course_name: grade}
        self.credits = {}       # {course_name: credit_hours}

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

    def add_credits(self, course_name, credits):
        if course_name in self.courses:
            self.credits[course_name] = credits
            print(f"{credits} credit hours added for {course_name}.")
        else:
            print(f"{self.name} is not enrolled in {course_name}, cannot assign credits.")

    def calculate_gpa(self):
        valid_grades = [grade for grade in self.courses.values() if grade is not None]
        if not valid_grades:
            return 0.0
        return sum(valid_grades) / len(valid_grades)

    def calculate_weighted_gpa(self):
        total_weighted = 0
        total_credits = 0
        for course, grade in self.courses.items():
            if grade is not None and course in self.credits:
                total_weighted += grade * self.credits[course]
                total_credits += self.credits[course]
        return total_weighted / total_credits if total_credits > 0 else 0.0

    def get_highest_grade(self):
        graded_courses = {course: grade for course, grade in self.courses.items() if grade is not None}
        if not graded_courses:
            return None, None
        highest_course = max(graded_courses, key=graded_courses.get)
        return highest_course, graded_courses[highest_course]

    def display_info(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print("Courses and Grades:")
        for course, grade in self.courses.items():
            credit_info = f" ({self.credits.get(course, 'N/A')} credits)"
            grade_display = grade if grade is not None else "Not graded"
            print(f"  - {course}{credit_info}: {grade_display}")
        print(f"GPA: {self.calculate_gpa():.2f}")
        print(f"Weighted GPA: {self.calculate_weighted_gpa():.2f}")

    def __str__(self):
        return f"Student({self.name}, ID: {self.student_id})"
