from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Student, Advisor, Course
from .forms import CourseForm, StudentForm, AdvisorForm, CourseSelectionForm, DropCourseForm


def index(request):
    students = Student.objects.order_by("lname")
    return render(request, "student/index.html", {"students": students})


def course_list(request):
    courses = Course.objects.all()
    return render(request, "student/course_list.html", {"courses": courses})


def advisor_list(request):
    advisors = Advisor.objects.all()
    return render(request, "student/advisor_list.html", {"advisors": advisors})


def course_detail(request, id):
    # Return object, if exists, or 404
    course = get_object_or_404(Course, pk=id)
    return render(request, "student/course_detail.html", {"course": course})


def advisor_detail(request, id):
    advisor = get_object_or_404(Advisor, pk=id)
    return render(request, "student/advisor_detail.html", {"advisor": advisor})


def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, "student/student_detail.html", {"student": student})


def add_student(request):
    if request.method == "POST":
        # Bind user input to the form
        student_form = StudentForm(request.POST)
        # Server-side validation
        if student_form.is_valid():
            # Save new student object
            new_student = student_form.save(commit=True)
            # Call 'student_detail path, pass it an argument
            return HttpResponseRedirect(reverse("student_detail", args=(new_student.id,)))
    else:
        # Empty form
        student_form = StudentForm()

    return render(request, "student/add_student.html", {"form": student_form})       


def edit_student(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == "POST":
        # Form bound with input data, form associated with 'student' object
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("student_detail", args=(student.id,)))
    else:
        form = StudentForm(instance=student)

    return render(request, "student/edit_student.html", {"form": form, "student": student})


def new_course(request):
    if request.method == "POST":
        # Form is populated with input data 
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("course_list"))
    else:
        form = CourseForm()
    return render(request, "student/add_course.html", {"form": form})


def edit_course(request, id):
    course = get_object_or_404(Course, pk=id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            updated_course = form.save()
            return HttpResponseRedirect(reverse("course_detail", args=(updated_course.id,)))
    form = CourseForm(instance=course)

    return render(request, "student/edit_course.html", {"form": form, "course": course})


def remove_course(request, id):
    course = get_object_or_404(Course, pk=id)
    if request.method == "POST":
        course.delete()
        return HttpResponseRedirect(reverse("course_list"))
    
    return render(request, "student/remove_course.html", {"course": course})


def new_advisor(request):
    if request.method == "POST":
        form = AdvisorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("advisor_list"))
    else:
        form = AdvisorForm()

    return render(request, "student/add_advisor.html", {"form": form})


def edit_advisor(request, id):
    advisor = get_object_or_404(Advisor, pk=id)

    if request.method == "POST":
        # Bind the POST with the current advisor instance
        form = AdvisorForm(request.POST, instance=advisor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("advisor_detail", args=(advisor.id,)))
    else:
        # Pre-populate form with advisor instance data
        form = AdvisorForm(instance=advisor)

    return render(request, "student/edit_advisor.html", {"form": form, "advisor": advisor})


def delete_advisor(request, advisor_id):
    advisor = get_object_or_404(Advisor, pk=advisor_id)
    if request.method == "POST":
        # Ensure all students referencing this advisor have their student_advisor set to NULL
        Student.objects.filter(student_advisor=advisor).update(student_advisor=None)
        advisor.delete()
        return HttpResponseRedirect(reverse("advisor_list"))
    return HttpResponseRedirect(reverse("advisor_list"))
    

def add_student_to_course(request, id):
    student = get_object_or_404(Student, pk=id)
    
    if request.method == "POST":
        form = CourseSelectionForm(request.POST)
        if form.is_valid():
            # Accessing the data from the 'course' field of the form
            course = form.cleaned_data['course']
            # Check if student already registered for course
            if course in student.courses.all():
                message = f"You've already registered for '{course.subject}'"
                context = {"message": message, "student": student}
                return render(request, 'student/duplicate_course.html', context)
            
            course.students.add(student)
            return HttpResponseRedirect(reverse('student_detail', args=(student.id,)))
    else:
        form = CourseSelectionForm()
        
    context = {"form": form, "student": student}
    return render(request, "student/add_student_to_course.html", context)


def deactivate_student(request, id):
    student = get_object_or_404(Student, pk=id)
    student.active = False
    student.save()
    messages.success(request, f"{student.fname} {student.lname} has been deactivated.")
    return HttpResponseRedirect(reverse('index'))


def drop_course(request, id):
    student = get_object_or_404(Student, pk=id)

    if request.method == "POST":
        form = DropCourseForm(request.POST, student=student)
        if form.is_valid():
            course = form.cleaned_data["course"]
            course.students.remove(student)
            messages.success(request, f"{student.fname} has dropped {course.subject}.")
            return HttpResponseRedirect(reverse("student_detail", args=(student.id,)))
    else:
        form = DropCourseForm(student=student)
    return render(request, "student/drop_course.html", {"student": student, "form": form})
