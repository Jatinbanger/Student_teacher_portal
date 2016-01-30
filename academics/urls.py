from django.conf.urls import include, url
from . import views

urlpatterns=[
    url(r'^$',  views.home, name='Home'),
    url(r'^login/$',    views.login_request,    name='Login'),
    url(r'^login/student/$',    views.login_request_student,    name='LoginStudent'),
    url(r'^logout/$', 	 		    views.logout_request,	name='Logout'),	
#    url(r'^register/$',                     views.register,             name='Register'),
#    url(r'^student/$',                      views.student,              name='Student'),
#    url(r'^teacher/$',                      views.teacher,              name='Teacher'),
    url(r'^teacher/attendance/$',           views.teacher_attendance,         name='Attendance'),
    url(r'^teacher/marks/$',                views.teacher_marks,              name='Marks'),
    url(r'^student/attendance/$',           views.student_attendance,         name='SAttendance'),
    url(r'^student/marks/$',                views.student_marks,              name='SMarks'),
#    url(r'^teachermarks/$',                  views.teachermarks,              name='TeacherMarks'),    
#    url(r'^teacherattendance/$',               views.teacherattendance,       name='TeacherAttendance'),
    


    url(r'^teacher/attendance/(?P<title>.*)/$',     views.teacher_attendance_group,     name='TeacherAttendanceGroup'),
    url(r'^teacher/a/save/$',              views.teacher_attendance_save,     name='TeacherAttendanceSave'),
    url(r'^teacher/marks/(?P<title>.*)/$',     views.teacher_marks_group,     name='TeacherMarksGroup'),
    url(r'^teacher/m/save/(?P<title>.*)/$',              views.teacher_marks_save,     name='TeacherMarksSave'),

#    url(r'^teacher/marks/(?P<title>.*)/$',          views.teacher_marks_group,          name='TeacherMarksGroup'),
    url(r'^student/attendance/(?P<title>.*)/$',     views.student_attendance_subject,     name='StudentAttendanceSubject'),
#    url(r'^student/marks/(?P<title>.*)/$',          views.student_marks_group,          name='StudentMarksGroup'),
]
