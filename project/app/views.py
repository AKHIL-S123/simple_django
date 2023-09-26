from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def signup(request):
    if  request.method == 'POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=fname
        myuser.save()
        messages.success(request,"Your account has been Successfully created")
        return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    if  request.method == 'POST':
        username=request.POST['username']
        pass1=request.POST['pass1']
        user = authenticate(request,username=username,password=pass1)
        print(username,pass1,user,"authenticate")
        if user is not None:
            login(request,user)
            return render(request,'home.html')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('home')

    return render(request,'signin.html')

def signout(request):
    logout(request)
    messages.success(request,"Logout successfully") 
    return render(request,'home.html')

def home(request):
    return render(request,'home.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})
