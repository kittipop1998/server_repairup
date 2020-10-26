from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import serializers
from django.db import models
from .models import UserProfile, User, Group



class RegisterSerializer(serializers.Serializer):
    # groups = models.ForeignKey(Group, on_delete=models.CASCADE)
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    is_staff = serializers.BooleanField(required=True, write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    "A user is already registered with this e-mail address.")
        return email


    def validate_password1(self, password):
        return get_adapter().clean_password(password)


    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                "The two password fields didn't match.")
        return data

    def get_cleaned_data(self):
        return {
            # 'groups': self.validated_data.get('groups', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'username': self.validated_data.get('username', ''),
            'is_staff': self.validated_data.get('is_staff', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        user.is_superuser = True
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        return user



    # def validate_username(self, username):
    #     username = get_adapter().clean_username(username)
    #     if not data.islower():
    #           raise from

    # def clean_username(self):
    #     data = self.cleaned_data['username']
    #     if not data.islower():
    #         raise forms.ValidationError("Usernames should be in lowercase")
    #     if '@' in data or '-' in data or '|' in data:
    #         raise forms.ValidationError("Usernames should not have special characters.")
    #     return data

    # def isnumeric(self, userNa):
    #     if userNa = username.isnumeric()
    #     return "{}".format(userNa).isdigit()
    #

    # def is_number(username):
    #     is_number = True
    #     try:
    #         #      v type-casting the number here as `complex`, instead of `float`
    #         num = complex(username)
    #         is_number = num == num
    #     except ValueError:
    #         is_number = False
    #     return is_number
    #
    # try:
    #     user_model.username = isnumeric['username']
    # except:
    #     pass
