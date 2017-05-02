# /payments/serializers.py
from payments.models import User
from rest_framework import serializers
PASSWORD_MAX_LENGTH = User._meta.get_field('password').max_length


class PasswordSerializer(serializers.Serializer):
    """
    Reset password serializer
    """
    password = serializers.CharField(max_length=PASSWORD_MAX_LENGTH)
    password2 = serializers.CharField(max_length=PASSWORD_MAX_LENGTH)

    def validate(self, data):
        pwd = data['password']
        pwd2 = data['password2']
        print("<validate> Password is:  ", pwd)
        print("<validate> Password2 is: ", pwd2)
        if pwd != pwd2:
            print("<validate> Passwords don't match!")
            raise serializers.ValidationError("Passwords don't match.")
        print("<validate> Passwords match!")
        return data

    def update(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)
        print("<update> Getting the password.")
        instance.set_password(instance.password)
        print("<update> Saving the password.")
        instance.save()
        print("<update> Saving the instance.")
        return instance
