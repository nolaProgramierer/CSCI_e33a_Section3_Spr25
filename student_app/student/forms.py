from django import forms
from django.forms import ModelForm

from .models import Student, Advisor, Course

#---------------------------------------------
# Model forms
#---------------------------------------------
# Inherits from ModelForm, form fields, validation, & save logic
class CourseForm(ModelForm):
    
    # Defines metadata for CourseForm
    class Meta:
        model = Course
        fields = ['dept','course_num', 'subject', 'description']

    # Customize initialization of CourseForm 
    def __init__(self, *args, **kwargs):
        # Call parent class (ModelForm) __init__ method
        super().__init__(*args, **kwargs)
        # 'visible_fields()' method provided by the form class
        for field in self.visible_fields():
            # Update HTML attributes on widget
            field.field.widget.attrs.update({
                "class": "form-control",
                "placeholder": f"Enter {field.label}"
            })
                

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['fname', 'lname', 'student_advisor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs.update({
                "class": "form-control",
                "placeholder": f"Enter {field.label}"
            })


class AdvisorForm(ModelForm):
    class Meta:
        model = Advisor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs.update({
                "class": "form-control",
                "placeholder": f"Enter {field.label}"
            })


#---------------------------------------------
# Form form
#---------------------------------------------
class CourseSelectionForm(forms.Form):
    # Define field for selecting an object from a queryset
    course = forms.ModelChoiceField(queryset=Course.objects.all(), 
        widget=forms.Select(attrs={"class": "form-control"}))


class DropCourseForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.none(), label="Select a course to drop")

    def __init__(self, *args, **kwargs):
        # Remove 'student' argument passed from views from kwargs
        student = kwargs.pop("student", None)
        super().__init__(*args, **kwargs)
        if student:
            self.fields["course"].queryset = student.courses.all()