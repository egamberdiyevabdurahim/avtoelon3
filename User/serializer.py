from rest_framework import serializers

from .models import User


class UserSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'status', 'phone', 'photo']
        read_only_fields = ['password']

    def create(self, validated_data):
        user = super().create(self.validated_data)
        user.set_password(validated_data.pop('password', None))
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.status = validated_data.get('status', instance.status)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.photo = validated_data.get('photo', instance.photo)
        # if not instance.password.check_password(validated_data['old_password']):
        #     raise serializers
        instance.password = validated_data.get('password', instance.password)
        instance.set_password(validated_data.pop('password', None))
        instance.save()
        return instance
