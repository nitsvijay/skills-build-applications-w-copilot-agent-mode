from django.test import TestCase
from django.contrib.auth.models import User
from .models import Activity

class ActivityTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.activity = Activity.objects.create(
            user=self.user,
            activity_type='run',
            date='2023-01-01',
            duration=30,
            distance=5.0,
            calories=300
        )

    def test_activity_creation(self):
        self.assertEqual(self.activity.user.username, 'testuser')
        self.assertEqual(self.activity.activity_type, 'run')