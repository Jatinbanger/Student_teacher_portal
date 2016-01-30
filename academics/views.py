from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Student
from .models import Teacher
from .models import Subject
from .models import Course_Dept
from .models import Group
from .models import TeacherRel
from .models import StudentRel
from .models import Attendance
from .models import Mark

def home(request):
	user = request.user
	if(user.is_authenticated()):
                state1='SAttendance'
                state2='SMarks'
                teachers = TeacherRel.objects.all()
                for teacher in teachers:
                        if user == teacher.user:
                                state1='Attendance'
                                state2='Marks'       
                return render(request,'dbms/After_Home.html',{'state1':state1,'state2':state2})
	else:
        	return render(request,'dbms/Home.html',{})


def login_request(request):
	state = "Log In"
	username = password = ''
	if request.POST:
		username = request.POST.get('t_id')
		password = request.POST.get('t_pwd')
		user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			user = request.user
			state1='SAttendance'
			state2='SMarks'
			teachers = TeacherRel.objects.all()
			for teacher in teachers:
                                if user == teacher.user:
                                        state1='Attendance'
                                        state2='Marks'
			return render(request, 'dbms/After_Home.html',{'user':user,'state1':state1,'state2':state2})
		else:
			state = "Your account is not active, please contact the site admin."
			return render(request,'dbms/Home.html',{'state':state, 'username': username})
	else:
		state = "Your username and/or password were incorrect."
		return render(request,'dbms/Home.html',{'state':state, 'username': username})


def login_request_student(request):
	state = "Log In"
	state1='SAttendance'
	state2='SMarks'
	username = password = ''
	if request.POST:
		username = request.POST.get('s_id')
		password = request.POST.get('s_pwd')
		user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			user = request.user
			return render(request, 'dbms/After_Home.html',{'user':user,'state1':state1,'state2':state2})
		else:
			state = "Your account is not active, please contact the site admin."
			return render(request,'dbms/Home.html',{'state':state, 'username': username})
	else:
		state = "Your username and/or password were incorrect."
	return render(request,'dbms/Home.html',{'state':state, 'username': username})
        
        


def logout_request(request):
	logout(request)
	return render(request,'dbms/Home.html',{})


def teacher_marks(request):
        user = request.user
        if(user.is_authenticated()):
                teacher = get_object_or_404(TeacherRel, user=user).teacher
                groups = Group.objects.filter(teacher=teacher)
                return render(request,'dbms/tmarks.html',{'groups':groups})
        else:
                return render(request, 'dbms/invalid.html',{})


def teacher_attendance(request):
        user = request.user
        if(user.is_authenticated()):
                teacher = get_object_or_404(TeacherRel, user=user).teacher
                groups = Group.objects.filter(teacher=teacher)
                return render(request,'dbms/tattendance.html',{'groups':groups})
        else:
                return render(request, 'dbms/invalid.html',{})
        


def student_marks(request):
        user = request.user
        if(user.is_authenticated()):
                student = get_object_or_404(StudentRel,user=user).student
                mark = student.marks
                return render(request,'dbms/smarks.html',{'mark':mark})
        else:
                return render(request, 'dbms/invalid.html',{})
        


def student_attendance(request):
        user = request.user
        if(user.is_authenticated()):
                student = get_object_or_404(StudentRel,user=user).student
                group = student.group_id
                subjects = Subject.objects.filter(pk=group.subject_Id.pk)
                return render(request,'dbms/sattendance.html',{'subjects':subjects})
        else:
                return render(request, 'dbms/invalid.html',{})
        


def teacher_attendance_group(request,title):
        user = request.user
        if(user.is_authenticated()):                
                group = get_object_or_404(Group,pk=title)
                students = Student.objects.filter(group_id=group)
                teacher = get_object_or_404(TeacherRel, user=user).teacher
                groups = Group.objects.filter(teacher=teacher)
                return render(request,'dbms/tattendance.html',{'students':students,'groups':groups,'group':group})
        else:
                return render(request, 'dbms/invalid.html',{})
        



def teacher_marks_group(request,title):
        user = request.user
        if(user.is_authenticated()):                
                group = get_object_or_404(Group,pk=title)
                students = Student.objects.filter(group_id=group)
                teacher = get_object_or_404(TeacherRel, user=user).teacher
                groups = Group.objects.filter(teacher=teacher)
                return render(request,'dbms/tmarks.html',{'students':students,'groups':groups,'group':group})
        else:
                return render(request, 'dbms/invalid.html',{})






def student_attendance_group(request):
        return render(request,'dbms/sattendgrp.html',{})



def student_attendance_subject(request,title):
        user = request.user
        if(user.is_authenticated()):
                student = get_object_or_404(StudentRel,user=user).student
                group = student.group_id
                subjects = Subject.objects.filter(pk=group.subject_Id.pk)
                subject = get_object_or_404(Subject,pk=title)
                attendances = Attendance.objects.filter(student_id=student).filter(subject_id=subject)
                return render(request,'dbms/sattendance.html',{'subjects':subjects,'attendances':attendances})
        else:
                return render(request, 'dbms/invalid.html',{})
        return render(request,'dbms/sattendgrp.html',{})








def student_marks_group(request):
        return render(request,'dbms/smarksgrp.html',{})



def teacher_attendance_save(request):
        user = request.user
        if(user.is_authenticated()):
                if request.POST:
                        teacher = get_object_or_404(TeacherRel, user=user).teacher
                        groups = Group.objects.filter(teacher=teacher)
                        roll_nos = request.POST.getlist('checks')
                        subject = get_object_or_404(Subject, teacher_Id=teacher)
                        group = get_object_or_404(Student,roll_no=int(roll_nos[0])).group_id
                        for roll_no in roll_nos:
                                student = get_object_or_404(Student, roll_no=int(roll_no))
                                attendance = Attendance(group_id=group,student_id=student,subject_id=subject,p_a='p',date=timezone.now().date())
                                attendance.save()
                        return home(request)
        else:
                return render(request,'dbms/invalid.html',{})




def teacher_marks_save(request,title):
        user = request.user
        if(user.is_authenticated()):
                if request.POST:
                        teacher = get_object_or_404(TeacherRel, user=user).teacher
                        groups = Group.objects.filter(teacher=teacher)
                        subject = get_object_or_404(Subject, teacher_Id=teacher)
                        group = get_object_or_404(Group, pk=title)
                        students = Student.objects.filter(group_id=group)
                        
                        for student in students:
                                mst1 = request.POST.get(str(student.roll_no) + '_1')
                                mst2 = request.POST.get(str(student.roll_no) + '_2')
                                evaluation = request.POST.get(str(student.roll_no) + '_3')
                                attend = request.POST.get(str(student.roll_no) + '_4')
                                sports = request.POST.get(str(student.roll_no) + '_5')
                                num = Mark(subject_id=subject, mst1=int(mst1), mst2=int(mst2), evaluation=int(evaluation), attendance=int(attend), sports=int(sports))
                                num.save()
                                student.marks = num
                                student.save()
                        return render(request,'dbms/tmarks.html',{'students':students,'groups':groups,'group':group,'num':num})
        return render(request,'dbms/invalid.html',{})









# Create your views here.
