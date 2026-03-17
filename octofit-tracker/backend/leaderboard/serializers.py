from rest_framework import serializers
from .models import Leaderboard

class LeaderboardSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'user_username', 'total_points', 'total_activities', 'total_distance', 'total_calories', 'updated_at']