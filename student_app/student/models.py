from django.db import models


class Student(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    active = models.BooleanField(default=True)
    student_advisor = models.ForeignKey("Advisor", on_delete=models.SET_NULL, null=True, related_name="advisees")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.lname}, {self.fname} (ID: {self.id})'
  
    def highest_course_num(self):
        courses = self.courses.all()
        return max(courses, key=lambda x: x.course_num) if courses else None

    def lowest_course_num(self):
        courses = self.courses.all()
        return min(courses, key=lambda y: y.course_num) if courses else None
    
    
class Course(models.Model):
    dept = models.CharField(max_length=3)
    course_num = models.IntegerField()
    subject = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    students = models.ManyToManyField(Student, blank=True, related_name="courses")

    class Meta:
        unique_together = ('dept', 'course_num')
        ordering = ['dept']

    def __str__(self):
        return f'{self.dept} {self.course_num}: {self.subject}'


class Advisor(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    
    class Meta:
        ordering = ['lname']
    
    def __str__(self):
        return f'{self.lname}, {self.fname}'
    

