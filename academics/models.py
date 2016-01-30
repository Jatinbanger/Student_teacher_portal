from django.db import models
from django.contrib.auth.models import User


class Course_Dept(models.Model):
    department_Name=models.CharField(max_length=30)
    course_Name=models.CharField(max_length=30)
    def	__str__(self):							
    		return	self.department_Name + ":" + self.course_Name




class Teacher(models.Model):
    tName=models.CharField(max_length=30)
    desgination=models.CharField(max_length=50)
    researchField=models.CharField(max_length=100)
    department=models.ForeignKey(Course_Dept)
    email=models.CharField(max_length=30,unique=True)
    contact=models.IntegerField()
    username=models.ForeignKey(User)
    def	__str__(self):							
    		return	self.tName




class TeacherRel(models.Model):
	user = models.ForeignKey(User)
	teacher = models.ForeignKey(Teacher)
	def __str__(self):							
    		return	self.teacher.tName



class Subject(models.Model):
    teacher_Id=models.ForeignKey(Teacher)
    subjectsName=models.CharField(max_length=30)
    def	__str__(self):							
    		return	self.subjectsName + ":" + self.teacher_Id.tName


class Group(models.Model):
    teacher=models.ForeignKey(Teacher)
    subject_Id=models.ForeignKey(Subject)
    groupName=models.CharField(max_length=20)
    year=models.IntegerField()
    def	__str__(self):							
    		return	self.groupName+":"+self.teacher.tName




class Mark(models.Model):
    subject_id=models.ForeignKey(Subject)
    mst1 = models.IntegerField(default=0)
    mst2 = models.IntegerField(default=0)
    evaluation = models.IntegerField(default=0)
    attendance = models.IntegerField(default=0)
    sports = models.IntegerField(default=0)



class Student(models.Model):
    group_id=models.ForeignKey(Group)
    roll_no=models.IntegerField()
    name=models.CharField(max_length=30)
    fatherName=models.CharField(max_length=30)
    motherName=models.CharField(max_length=30)
    dob=models.DateField()
    regdId=models.CharField(max_length=15, primary_key=True)
    address=models.CharField(max_length=40)
    contact=models.IntegerField()
    session=models.CharField(max_length=20)
    course_Dept=models.ForeignKey(Course_Dept)
    # count = models.IntegerField()
    username=models.ForeignKey(User)
    marks=models.ForeignKey(Mark,null=True)
    def	__str__(self):							
    		return	self.name


class StudentRel(models.Model):
	user = models.ForeignKey(User)
	student = models.ForeignKey(Student)
	def	__str__(self):							
    		return	self.student.name



class Attendance(models.Model):
    group_id=models.ForeignKey(Group)
    student_id=models.ForeignKey(Student)
    subject_id=models.ForeignKey(Subject)
    p_a = models.CharField(max_length=1)
    date=models.DateField()


    
    
    

# Create your models here.
