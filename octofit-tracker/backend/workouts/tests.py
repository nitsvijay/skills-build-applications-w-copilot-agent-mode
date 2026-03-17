from django.test import TestCase
from django.contrib.auth.models import User
from .models import WorkoutPlan, Exercise

class WorkoutTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.workout_plan = WorkoutPlan.objects.create(name='Test Plan', user=self.user)
        self.exercise = Exercise.objects.create(
            workout_plan=self.workout_plan,
            name='Push-ups',
            sets=3,
            reps=10
        )

    def test_workout_plan_creation(self):
        self.assertEqual(self.workout_plan.name, 'Test Plan')
        self.assertEqual(self.workout_plan.user.username, 'testuser')