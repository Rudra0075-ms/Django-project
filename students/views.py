from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q

from .models import Student
from .forms import StudentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def home(request):

    total_students = Student.objects.count()

    return render(
        request,
        'students/home.html',
        {'total_students': total_students}
    )

@login_required
def student_list(request):

    query = request.GET.get('q')
    sort = request.GET.get('sort', 'id')

    if query:
        students = Student.objects.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query)
        )
    else:
        students = Student.objects.all()

    if sort == 'name':
        students = students.order_by('name')

    elif sort == 'age':
        students = students.order_by('age')

    else:
        students = students.order_by('id')

    paginator = Paginator(students, 5)

    page_number = request.GET.get('page')

    students = paginator.get_page(page_number)

    return render(
        request,
        'students/student_list.html',
        {
            'students': students,
            'query': query,
            'sort': sort
        }
    )

@login_required
def add_student(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('student_list')

    else:
        form = StudentForm()

    return render(
        request,
        'students/add_student.html',
        {'form': form}
    )

@login_required
def edit_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == 'POST':

        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student_list')

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        'students/edit_student.html',
        {'form': form}
    )


@login_required
def delete_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('student_list')

    return redirect('student_list')


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        return render(
            request,
            'students/login.html',
            {'error': 'Invalid username or password.'}
        )

    return render(request, 'students/login.html')    

def signup_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(
                request,
                'students/signup.html',
                {'error': 'Username already exists.'}
            )

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('login')

    return render(request, 'students/signup.html')


def logout_view(request):
    logout(request)
    return redirect('login')    