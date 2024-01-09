from rest_framework import serializers

from .models import User


class UserSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'status', 'phone', 'photo']
        read_only_fields = ['password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data('password'))
        user.save()
        return user
