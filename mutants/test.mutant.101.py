import unittest
from LMS import Course, Student, Instructor, LMS

class TestCourse(unittest.TestCase):
    def setUp(self):
        self.course = Course(1, "Python Programming", "Introduction to Python")
        self.student = Student(1, "John Doe")
        self.course.add_student(self.student)

    def test_add_student(self):
        self.assertIn(self.student, self.course.students)
        self.assertEqual(self.course.progress[self.student], 0)

    def test_remove_student(self):
        self.course.remove_student(self.student)
        self.assertNotIn(self.student, self.course.students)
        self.assertNotIn(self.student, self.course.progress)

    def test_update_progress(self):
        self.course.update_progress(self.student, 50)
        self.assertEqual(self.course.progress[self.student], 50)

    def test_complete_notification(self):
        with self.assertLogs(level='INFO') as log:
            self.course.update_progress(self.student, 100)
            self.course.complete_notification(self.student)
            self.assertIn("has completed the course", log.output[-1])

    def test_grade_distribution(self):
        distribution = self.course.grade_distribution()
        self.assertEqual(distribution[0], 1)

    def test_attendance_tracking(self):
        attendance = self.course.attendance_tracking()
        self.assertTrue(attendance[self.student.name])

    def test_review_system(self):
        reviews = self.course.review_system()
        self.assertIn("Excellent course!", reviews)

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student(1, "John Doe")
        self.course = Course(1, "Python Programming", "Introduction to Python")

    def test_enroll(self):
        self.student.enroll(self.course)
        self.assertIn(self.student, self.course.students)

    def test_drop_course(self):
        self.student.enroll(self.course)
        self.student.drop_course(self.course)
        self.assertNotIn(self.student, self.course.students)

class TestInstructor(unittest.TestCase):
    def setUp(self):
        self.instructor = Instructor(1, "Jane Smith")
        self.student = Student(1, "John Doe")
        self.course = self.instructor.create_course( "Python Programming",1, "Introduction to Python")
        self.course.add_student(self.student)

    def test_create_course(self):
        self.assertIn(self.course, self.instructor.courses)

    def test_assign_grade(self):
        self.instructor.assign_grade(self.course, self.student, 90)
        self.assertEqual(self.course.progress[self.student], 90)

class TestLMS(unittest.TestCase):
    def setUp(self):
        self.lms = LMS()
        self.instructor = Instructor(1, "Jane Smith")
        self.student = Student(1, "John Doe")
        self.course = Course(1, "Python Programming", "Introduction to Python")

    def test_add_instructor(self):
        self.lms.add_instructor(self.instructor)
        self.assertIn(self.instructor, self.lms.instructors)

    def test_add_student(self):
        self.lms.add_student(self.student)
        self.assertIn(self.student, self.lms.students)

    def test_register_course(self):
        self.lms.register_course(self.course)
        self.assertIn(self.course, self.lms.courses)

class TestCourseAdvanced(unittest.TestCase):
    def setUp(self):
        self.course = Course(2, "Advanced Python", "Deep dive into Python")
        self.student1 = Student(2, "Alice Wonderland")
        self.student2 = Student(3, "Bob Builder")

    def test_multiple_students(self):
        self.course.add_student(self.student1)
        self.course.add_student(self.student2)
        self.assertEqual(len(self.course.students), 2)
        self.course.remove_student(self.student1)
        self.assertIn(self.student2, self.course.students)
        self.assertNotIn(self.student1, self.course.students)

    def test_progress_updates(self):
        self.course.add_student(self.student1)
        self.course.update_progress(self.student1, 75)
        self.assertEqual(self.course.get_student_progress(self.student1), 75)
        self.course.update_progress(self.student1, 150)  # Test over 100%
        self.assertEqual(self.course.get_student_progress(self.student1), 150)

    def test_nonexistent_student_progress_update(self):
        self.course.update_progress(self.student2, 50)
        self.assertEqual(self.course.get_student_progress(self.student2), "Student not enrolled")

    def test_attendance_multiple_days(self):
        self.course.add_student(self.student1)
        # Assuming functionality to track multiple days' attendance
        attendance = self.course.attendance_tracking()
        self.assertTrue(attendance[self.student1.name])

    def test_invalid_progress_update(self):
        self.course.add_student(self.student1)
        with self.assertRaises(ValueError):
            self.course.update_progress(self.student1, -10)  # Invalid progress

class TestInstructorAdvanced(unittest.TestCase):
    def setUp(self):
        self.instructor = Instructor(2, "Dr. Seuss")
        self.course = self.instructor.create_course(3, "Literature", "Exploring classics")

    def test_assign_to_multiple_courses(self):
        new_course = self.instructor.create_course(4, "Writing", "Creative writing course")
        self.assertEqual(len(self.instructor.courses), 2)
        self.assertIn(new_course, self.instructor.courses)

    def test_instructor_course_removal(self):
        self.instructor.courses.remove(self.course)
        self.assertNotIn(self.course, self.instructor.courses)

class TestLMSSystem(unittest.TestCase):
    def setUp(self):
        self.lms = LMS()
        self.instructor = Instructor(3, "Mr. Miyagi")
        self.student = Student(4, "Daniel San")
        self.course = Course(4, "Karate 101", "Basics of Karate")

    def test_complex_scenario(self):
        # Add multiple users and courses
        self.lms.add_instructor(self.instructor)
        self.lms.add_student(self.student)
        self.lms.register_course(self.course)
        self.student.enroll(self.course)
        self.assertEqual(len(self.lms.courses), 1)
        self.assertEqual(len(self.lms.students), 1)
        self.assertEqual(len(self.lms.instructors), 1)

    def test_course_registration_and_unregistration(self):
        self.lms.register_course(self.course)
        self.lms.courses.remove(self.course)
        self.assertNotIn(self.course, self.lms.courses)

    def test_error_handling_nonexistent_user(self):
        result = self.lms.record_activity("nonuser", "2024-01-01", "Jogging", 30, 300)
        self.assertEqual(result, "User not found.")

if __name__ == '__main__':
    unittest.main()