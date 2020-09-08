from django.urls import path

from attendance_server.views.authentication import CustomAuthToken
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

LIST = {
    'get': 'list'
}

RETRIEVE = {
    'get': 'retrieve'
}

# course_list = CourseReadViewSet.as_view(LIST)
# course_detail = CourseReadViewSet.as_view(RETRIEVE)
#
# course_class_list = CourseClassReadViewSet.as_view(LIST)
# course_class_detail = CourseClassReadViewSet.as_view(RETRIEVE)

course_teacher_list = CourseTeacherViewSet.as_view(LIST)
course_teacher_detail = CourseTeacherViewSet.as_view(RETRIEVE)

course_schedule_list = CourseScheduleViewSet.as_view(LIST_AND_CREATE)
course_schedule_detail = CourseScheduleViewSet.as_view(DETAILS_UPDATE_DELETE)

attendance_list = AttendanceViewSet.as_view(LIST_AND_CREATE)
attendance_detail = AttendanceViewSet.as_view(DETAILS_UPDATE_DELETE)

urlpatterns = [
    # path('course/', course_list, name='teacher-course-list'),
    # path('course/<int:pk>/', course_detail, name='teacher-course-detail'),
    # path('course_class/', course_class_list, name='course-class-list'),
    # path('course_class/<int:pk>/', course_class_detail, name='course-class-detail'),
    path('course-teacher/', course_teacher_list, name='teacher-course-teacher-list'),
    path('course-teacher/<int:pk>/', course_teacher_detail, name='teacher-course-teacher-detail'),
    path('course-schedule/', course_schedule_list, name='teacher-course-schedule-list'),
    path('course-schedule/<int:pk>/', course_schedule_list, name='teacher-course-schedule-detail'),
    path('attendance/', attendance_list, name='teacher-attendance-list'),
    path('attendance/<int:pk>/', attendance_detail, name='teacher-attendance-detail'),
    path('attendance/absent/', AbsentStudentView.as_view(), name='teacher-attendance-absent-list'),
    path('attendance/present/', PresentStudentView.as_view(), name='teacher-attendance-present-list'),
    path('attendance/late/', LateStudentView.as_view(), name='teacher-attendance-late-list'),
    path('login/', CustomAuthToken.as_view(), name='teacher-login'),
    path('student/', StudentProfileViewByStudentId.as_view(), name='get-student-by-student_id'),
    path('override-attendance/', OverrideAttendanceView.as_view(), name='override-attendance'),
]
