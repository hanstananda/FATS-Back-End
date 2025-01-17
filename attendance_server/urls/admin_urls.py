from django.urls import path

from attendance_server.views.admin_views import *

app_name = 'attendance_server'

LIST_AND_CREATE = {
    'get': 'list',
    'post': 'create'
}
DETAILS_UPDATE_DELETE = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

user_list = UserViewSetAdmin.as_view(LIST_AND_CREATE)
user_detail = UserViewSetAdmin.as_view({
    'get': 'retrieve'
})

course_list = CourseViewSetAdmin.as_view(LIST_AND_CREATE)
course_detail = CourseViewSetAdmin.as_view(DETAILS_UPDATE_DELETE)

course_class_list = CourseClassViewSetAdmin.as_view(LIST_AND_CREATE)
course_class_detail = CourseClassViewSetAdmin.as_view(DETAILS_UPDATE_DELETE)

course_teacher_list = CourseTeacherViewSetAdmin.as_view(LIST_AND_CREATE)
course_teacher_detail = CourseTeacherViewSetAdmin.as_view(DETAILS_UPDATE_DELETE)

course_student_list = CourseStudentViewSetAdmin.as_view(LIST_AND_CREATE)
course_student_detail = CourseScheduleViewSetAdmin.as_view(DETAILS_UPDATE_DELETE)

course_schedule_list = CourseScheduleViewSetAdmin.as_view(LIST_AND_CREATE)
course_schedule_detail = CourseScheduleViewSetAdmin.as_view(DETAILS_UPDATE_DELETE)

attendance_list = AttendanceViewSetAdmin.as_view(LIST_AND_CREATE)
attendance_detail = AttendanceViewSetAdmin.as_view(DETAILS_UPDATE_DELETE)

urlpatterns = [
    path('user/', user_list, name='admin-user-list'),
    path('user/<int:pk>/', user_detail, name='admin-user-detail'),
    path('course/', course_list, name='admin-course-list'),
    path('course/<int:pk>/', course_detail, name='admin-course-detail'),
    path('course-class/', course_class_list, name='admin-course-class-list'),
    path('course-class/<int:pk>/', course_class_detail, name='admin-course-class-detail'),
    path('course-teacher/', course_teacher_list, name='admin-course-teacher-list'),
    path('course-teacher/<int:pk>/', course_teacher_detail, name='admin-course-teacher-detail'),
    path('course-student/', course_student_list, name='admin-course-student-list'),
    path('course-student/<int:pk>/', course_student_detail, name='admin-course-student-detail'),
    path('course-schedule/', course_schedule_list, name='admin-course-schedule-list'),
    path('course-schedule/<int:pk>/', course_schedule_list, name='admin-course-schedule-detail'),
    path('attendance/', attendance_list, name='admin-attendance-list'),
    path('attendance/<int:pk>/', attendance_detail, name='admin-attendance-detail'),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]
