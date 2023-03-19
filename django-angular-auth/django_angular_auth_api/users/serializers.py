from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
        )
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'email', 'bio', 'profile_pic', 'attempts', 'score')
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def patch(self, instance, validated_data):
        instance.attempts = validated_data.get('attempts', instance.score)
        instance = super().update(instance, validated_data)
        return instance

