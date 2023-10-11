from django.utils.functional import lazy
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'nickname', 'birthdate', 'password',)


class ChangePasswordSerializer(serializers.ModelSerializer):
    pw = serializers.CharField(
        write_only=True,
        required=True,
        # validators=[validate_password]
    )
    pw2 = serializers.CharField(write_only=True, required=True)
    old = serializers.CharField(write_only=True, required=True)


    class Meta:
        model = User
        fields = ('old', 'pw', 'pw2')


    def validate(self, attrs):
        if attrs['pw'] != attrs['pw2']:
            raise serializers.ValidationError(
                {"password": _('Password fields did not match.')}
            )

        return attrs
    

    def validate_old(self, value):
        user = self.context['request'].user

        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old": _('Old password is not correct.')}
            )
        
        return value
    

    def update(self, instance, validated_data):
        instance.set_password(validated_data['pw'])
        instance.save()

        return instance


class UserUpdateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    nickname = serializers.CharField(required=True)
    birthdate = serializers.DateField(required=True)


    class Meta:
        model = User
        fields = ('username', 'email', 'nickname', 'birthdate')


    def validate_username(self, value):
        user = self.context['request'].user

        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError(
                {"username": _('User with this username already exists.')}
            )

        return value


    def validate_email(self, value):
        user = self.context['request'].user

        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError(
                {"email": _('User with this email already exists.')}
            )

        return value


    def validate_nickname(self, value):
        user = self.context['request'].user

        if User.objects.exclude(pk=user.pk).filter(nickname=value).exists():
            raise serializers.ValidationError(
                {"nickname": _('User with this nickname already exists.')}
            )

        return value


    def update(self, instance, validated_data):
        if 'username' in validated_data:
            instance.username = validated_data['username']
        if 'email' in validated_data:
            instance.email = validated_data['email']
        if 'nickname' in validated_data:
            instance.nickname = validated_data['nickname']
        instance.save()

        return instance