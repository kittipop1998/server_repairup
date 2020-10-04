from rest_framework import serializers
from .models import Dormitory, RoomType, Room, UserProfile, RepairType, Repair


class DormitorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dormitory
        fields = ['nameDo']


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['nameTy']


class RoomSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer(read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'nameRo', 'room_type']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UserProfile
        exclude = ('password', 'groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser')


class RepairTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairType
        fields = ['nameRe']


class RepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repair
        fields = ['status_choices', 'contact', 'desc', 'created_date',
                  'status', 'request_date',
                  'completed_data', 'approve_data',
                  'image', 'user_profile']


class RepairTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairType
        fields = ['nameRe']
