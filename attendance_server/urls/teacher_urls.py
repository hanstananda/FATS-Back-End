from django.urls import path

from attendance_server.views.teacher_views import *

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


course_teacher_list = CourseTeacherViewSet.as_view({
    'get': 'list'
})
course_teacher_detail = CourseTeacherViewSet.as_view({
    'get': 'retrieve'
})

course_schedule_list = CourseScheduleViewSet.as_view(LIST_AND_CREATE)
course_schedule_detail = CourseScheduleViewSet.as_view(DETAILS_UPDATE_DELETE)

attendance_list = AttendanceViewSet.as_view(LIST_AND_CREATE)
attendance_detail = AttendanceViewSet.as_view(DETAILS_UPDATE_DELETE)


urlpatterns = [
    path('course-teacher/', course_teacher_list, name='teacher-course-teacher-list'),
    path('course-teacher/<int:pk>/', course_teacher_detail, name='teacher-course-teacher-detail'),
    path('course-schedule/', course_schedule_list, name='teacher-course-schedule-list'),
    path('course-schedule/<int:pk>/', course_schedule_list, name='teacher-course-schedule-list'),
    path('attendance/', attendance_list, name='teacher-attendance-list'),
    path('attendance/<int:pk>/', attendance_detail, name='teacher-attendance-detail'),
]
