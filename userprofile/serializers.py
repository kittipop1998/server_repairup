from rest_framework import serializers
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


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UserProfile
        exclude = ('id', 'password', 'groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser')


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

<<<<<<< HEAD

=======
>>>>>>> ca61a92342528267e9136f25a02f90f0b9032db9
# class RepairTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RepairType
#         fields = ['nameRe']
