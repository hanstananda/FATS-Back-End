from django.test import TestCase
from attendance_server.models import TeacherProfile
from django.contrib.auth.models import User


class TeacherLoginTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="admin", password="admin")
        TeacherProfile.objects.create(user=user)

    def test_model_created(self):
        teacher = TeacherProfile.objects.filter(user=User.objects.all().first())
        assert(teacher.exists())

