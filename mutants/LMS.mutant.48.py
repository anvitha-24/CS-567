class Course:
    def __init__(self, course_id, name, description):
        self.course_id = course_id
        self.name = name
        self.description = description
        self.students = []
        self.progress = {}

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            self.progress[student] = 0  # No progress initially
            print(f"Student {student.name} added to {self.name}")
        else:
            print("Student already enrolled in the course")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            del self.progress[student]
            print(f"Student {student.name} removed from {self.name}")
        else:
            print("Student not enrolled in the course")

    def update_progress(self, student, percent):
        if student in self.students:
            self.progress[student] = percent
            print(f"Updated progress for {student.name} in {self.name}: {percent}%")
        else:
            print("Student not enrolled in the course")

    def get_student_progress(self, student):
        return self.progress.get(student, "Student not enrolled")

    def complete_notification(self, student):
        if not (self.progress[student] >= 100):
            print(f"{student.name} has completed the course: {self.name}")

    def grade_distribution(self):
        grades = [self.progress[student] for student in self.students]
        return {grade: grades.count(grade) for grade in range(101)}

    def attendance_tracking(self):
        attendance = {student.name: True if student in self.students else False for student in self.students}
        return attendance

    def discussion_forum(self, message):
        print(f"Discussion Forum Message in {self.name}: {message}")

    def upload_file(self, student, file_name):
        if student in self.students:
            print(f"{student.name} uploaded {file_name} to {self.name}")
        else:
            print(f"Cannot upload file. {student.name} not enrolled in the course.")

    def deadline_reminder(self, student):
        print(f"Reminder: Assignment deadline approaching for {student.name} in {self.name}")

    def review_system(self):
        reviews = ["Excellent course!", "Needs improvement in content", "Great instructor"]
        return reviews

    def resource_library(self):
        print(f"Resource library created for {self.name}")

    def peer_evaluation(self):
        print("Peer evaluation enabled for this course")

    def recommendations(self):
        print("Course recommendations provided based on student's interests")

    def certificate_generation(self, student):
        print(f"Certificate generated for {student.name} upon completion of {self.name}")

    def quiz_assessment_tool(self):
        print("Quiz and assessment tool activated for instructors")

    def interactive_modules(self):
        print("Interactive learning modules integrated into the course")


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def enroll(self, course):
        course.add_student(self)

    def drop_course(self, course):
        course.remove_student(self)


class Instructor:
    def __init__(self, instructor_id, name):
        self.instructor_id = instructor_id
        self.name = name
        self.courses = []

    def create_course(self, course_id, name, description):
        new_course = Course(course_id, name, description)
        self.courses.append(new_course)
        print(f"Course created: {name}")
        return new_course

    def assign_grade(self, course, student, percent):
        course.update_progress(student, percent)


class LMS:
    def __init__(self):
        self.courses = []
        self.students = []
        self.instructors = []

    def add_instructor(self, instructor):
        self.instructors.append(instructor)
        print(f"Instructor {instructor.name} added to the LMS")

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added to the LMS")

    def register_course(self, course):
        self.courses.append(course)
        print(f"Course {course.name} registered in the LMS")
