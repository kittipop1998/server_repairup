from rest_framework import serializers
from django.db import models
from django import forms
from django.contrib.auth.models import Group, User
from .models import Dormitory, RoomType, Room, UserProfile, RepairType, Repair


class DormitorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dormitory
        fields = ['id', 'nameDo']


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['id', 'nameTy']


class RoomSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer(read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'nameRo', 'room_type']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = UserProfile

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(read_only=True, many=True)

    class Meta:
        model = User
        exclude = ('id', 'password', 'user_permissions', 'is_staff', 'is_active', 'is_superuser')
class RepairTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairType
        fields = ['id', 'nameRe']


class RepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repair
        fields = ['id', 'status_choices', 'contact', 'desc', 'created_date',
                  'status', 'request_date',
                  'completed_data', 'approve_data',
                  'image', 'user_profile']

# class UserRegisterView(serializers.ModelSerializer):
#     groups = GroupSerializer(read_only=True, many=True)
#     class Meta:
        # model = User
        # fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'groups']
