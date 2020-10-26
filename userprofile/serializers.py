from rest_framework import serializers, filters
from django.db import models
from django import forms
from django.contrib.auth.models import Group, User
from .models import Dormitory, RoomType, Room, UserProfile, RepairType, Repair
import django_filters.rest_framework


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
    dormitory = DormitorySerializer(read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'nameRo', 'room_type', 'dormitory']


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
    userprofile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        exclude = ('password', 'user_permissions', 'is_staff', 'is_active', 'is_superuser')


class RepairTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairType
        fields = ['id', 'nameRe']


class RepairSerializer(serializers.ModelSerializer):
    userprofile = UserSerializer(read_only=True, source='user')
    room_data = RoomSerializer(source='room', read_only=True)
    repairType_data = RepairTypeSerializer(source='repair_type', read_only=True)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id']
    ordering = ['-id']

    class Meta:
        model = Repair
        fields = '__all__'

cl

# class UserRegisterView(serializers.ModelSerializer):
#     groups = GroupSerializer(read_only=True, many=True)
#     class Meta:
# model = User
# fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'groups']
