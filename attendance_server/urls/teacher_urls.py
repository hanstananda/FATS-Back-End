from django.urls import path

from attendance_server.views.teacher_views import CourseTeacherViewSet

course_teacher_list = CourseTeacherViewSet.as_view({
    'get': 'list'
})
course_teacher_detail = CourseTeacherViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('course-teacher/', course_teacher_list, name='course-teacher-list'),
    path('course-teacher/<int:pk>/', course_teacher_detail, name='course-teacher-detail'),
]
