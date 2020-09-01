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
course_detail = UserViewSetAdmin.as_view(DETAILS_UPDATE_DELETE)

course_schedule_list = CourseScheduleViewSetAdmin.as_view(LIST_AND_CREATE)
course_schedule_detail = CourseScheduleViewSetAdmin.as_view(DETAILS_UPDATE_DELETE)

attendance_list = AttendanceViewSetAdmin.as_view(LIST_AND_CREATE)
attendance_detail = AttendanceViewSetAdmin.as_view(DETAILS_UPDATE_DELETE)

urlpatterns = [
    path('user/', user_list, name='user-list'),
    path('user/<int:pk>/', user_detail, name='user-detail'),
    path('course/', course_list, name='course-list'),
    path('course/<int:pk>/', course_detail, name='course-detail'),
    path('course-schedule/', course_schedule_list, name='course-schedule-list'),
    path('course-schedule/<int:pk>/', course_schedule_list, name='course-schedule-list'),
    path('attendance/', attendance_list, name='attendance-list'),
    path('attendance/<int:pk>/', attendance_detail, name='attendance-detail'),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]