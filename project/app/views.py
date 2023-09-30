from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,permission_required,user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import Group, Permission
# from .models import custom_permission


def is_teacher(user):
    return user.groups.filter(name='teacher').exists()

def is_principal(user):
    return user.groups.filter(name='principal').exists()

def is_teacher_or_principal(user):
    return is_teacher(user) or is_principal(user)

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
        group_name = request.POST.get('group')
        group = Group.objects.get(name=group_name)
        myuser.groups.add(group) 
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
            # return redirect('student_list')
            print(user.get_all_permissions())

            if user.has_perm('app.view_student'):
                print(111111111111111111111111111111)
            else:
                print(22222222222222222222222222)
            return redirect('student_list')
        else:
            messages.error(request,"Invalid credentials")
           

    return render(request,'signin.html')

@login_required
def signout(request):
    logout(request)
    messages.success(request,"Logout successfully") 
    return redirect('signin')

@login_required
def home(request):
    students = Student.objects.all()
    return render(request,'student_list.html',{'students':students})





@user_passes_test(is_teacher_or_principal,login_url='error') 
# @staff_member_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})
    
@user_passes_test(is_teacher_or_principal,login_url='error')
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

@user_passes_test(is_principal,login_url='error')
# @permission_required('app.can_delete_student', raise_exception=True)
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})

from django.shortcuts import render

def custom_permission_denied(request, exception=None):
    return render(request, '403.html', status=403)
