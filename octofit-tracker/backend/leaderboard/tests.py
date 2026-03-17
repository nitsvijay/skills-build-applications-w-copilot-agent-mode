from django.test import TestCase
from django.contrib.auth.models import User
from .models import Leaderboard

class LeaderboardTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.leaderboard = Leaderboard.objects.create(user=self.user, total_points=100)

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.user.username, 'testuser')
        self.assertEqual(self.leaderboard.total_points, 100)