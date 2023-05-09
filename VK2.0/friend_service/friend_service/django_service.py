# models.py
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Friendship(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    )

    from_user = models.ForeignKey(User, related_name='outgoing_friendships', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='incoming_friendships', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f'{self.from_user.username} -> {self.to_user.username}'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class FriendshipSerializer(serializers.ModelSerializer):
    from_user = UserSerializer()
    to_user = UserSerializer()

    class Meta:
        model = Friendship
        fields = ['id', 'from_user', 'to_user', 'status']

