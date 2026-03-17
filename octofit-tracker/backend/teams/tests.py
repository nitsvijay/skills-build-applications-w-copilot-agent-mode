from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team

class TeamTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='12345')
        self.user2 = User.objects.create_user(username='user2', password='12345')
        self.team = Team.objects.create(name='Test Team', creator=self.user1)
        self.team.members.add(self.user1, self.user2)

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.creator.username, 'user1')