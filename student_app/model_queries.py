# Import models from student app
from student.models import *

# 1) Create a new advisor
advisor1 = Advisor(fname="Gergory", lname="Patel")
advisor1.save()

# 2) Create a new course
course1 = Course(dept="MUS", course_num=400, subject="Intro to Wagner")
course1.save()

# 3) Create a new student
student1 = Student(fname="Isabella", lname="Cohn", student_advisor=advisor1)
student1.save()
student1

# 4) Assign a student to the course
course1.students.add(student1)
course1

# 5) Make another student
student2 = Student(fname="Ethan", lname="Ramierz", student_advisor=advisor1)
student2.save()
student2

# 6) Add this student to the course from the other side of the relationship
student2.courses.add(course1)
student2.courses.all()

# 7) Find all courses a student is enrolled in
student1.courses.all()

# 8) Find all students in a particular course
course1.students.all()

# 9)Show all advisees of Albert Einstein
advisor1.advisees.all()

# 10) Find all active student
active_students = Student.objects.filter(active=True)
active_students

# 11) Find students with no advisor
students_wo_advisors = Student.objects.filter(student_advisor__isnull=True)
students_wo_advisors

# 12) Find all students enrolled in at least one course
students_with_courses = Student.objects.filter(courses__isnull=False).distinct()
students_with_courses

# 13) Return all of Albert's advisees whose last names begin with "G"
advisor1.advisees.filter(lname__startswith="B")

# 14) Add another course
course2 = Course(dept="PHY", course_num=301, subject="Quantum Mechanics")
course2.save()

# 15) Add course to a student
student1.courses.add(course2)

# 16) Return all of a students courses
student1.courses.all()

# 17) Return the highest course number of a student
student1.highest_course_num()

# 18) Return the lowest course number of a student
student1.lowest_course_num()

# 19) Retrieve all students enrolled in a particular course and advised by a particular advisor
students_advised_and_enrolled = advisor1.advisees.filter(courses=course1)
students_advised_and_enrolled


