from datetime import timedelta

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from attendance_server.constants import LATE_ATTENDANCE_CUTOFF_MINUTES
from attendance_server.models import *


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseClass
        fields = '__all__'


class CourseScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSchedule
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


class AttendanceTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

    def create(self, validated_data):
        if 'late' not in validated_data:
            course_schedule = CourseSchedule.objects.get(id=validated_data['course_schedule'].id)
            late = timezone.now() > (course_schedule.open_time + timedelta(minutes=LATE_ATTENDANCE_CUTOFF_MINUTES))
            validated_data['late'] = late
        attendance = Attendance.objects.create(**validated_data)
        attendance.save()
        return attendance


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'


class StudentProfileDetailedSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = StudentProfile
        fields = '__all__'


class CourseTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTeacher
        fields = '__all__'


class CourseStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseStudent
        fields = '__all__'


class CourseClassDetailedSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = CourseClass
        fields = '__all__'


class CourseTeacherDetailedSerializer(serializers.ModelSerializer):
    course_class = CourseClassDetailedSerializer()

    # course_info = CourseSerializer()

    class Meta:
        model = CourseTeacher
        fields = ('course_class', )


class TakeAttendanceSerializer(serializers.Serializer):
    raw_picture = serializers.CharField(max_length=10000000)
    session_id = serializers.IntegerField()
