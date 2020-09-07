from django.test import TestCase
from django.urls import reverse

from attendance_server.models import TeacherProfile
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status


class TeacherLoginTestCase(TestCase):
    USERNAME = "teacher"
    PASSWORD = "teacher"

    def setUp(self):
        user = User.objects.create_user(username=self.USERNAME, password=self.PASSWORD)
        TeacherProfile.objects.create(user=user)

    def test_model_created(self):
        user = User.objects.filter(username=self.USERNAME).first()
        teacher = TeacherProfile.objects.filter(user=user)
        assert (teacher.exists())

    def test_view(self):
        client = APIClient()
        response = client.post(reverse('teacher-login'), {'username': self.USERNAME, 'password': self.PASSWORD},
                               format='json')
        assert (response.status_code == status.HTTP_200_OK)
