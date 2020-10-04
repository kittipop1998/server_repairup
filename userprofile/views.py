from django.shortcuts import render
from rest_framework import viewsets
from .models import Dormitory, RoomType, Room, UserProfile, RepairType, Repair
from .serializers import DormitorySerializer, RoomTypeSerializer, RoomSerializer, UserProfileSerializer, \
    RepairTypeSerializer, RepairSerializer


# Create your views here.
class DormitoryViewSet(viewsets.ModelViewSet):
    queryset = Dormitory.objects.all()
    serializer_class = DormitorySerializer


class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class RepairTypeViewSet(viewsets.ModelViewSet):
    queryset = RepairType.objects.all()
    serializer_class = RepairTypeSerializer


class RepairViewSet(viewsets.ModelViewSet):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer
