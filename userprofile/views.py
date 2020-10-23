from django.shortcuts import render
from rest_framework import viewsets
from rest_auth.registration.views import RegisterView
from rest_auth.views import UserDetailsView
from django.conf.urls.static import static
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import  status
from django.contrib.auth.models import Group, User
from .models import Dormitory, RoomType, Room, UserProfile, RepairType, Repair
from .serializers import DormitorySerializer, RoomTypeSerializer, RoomSerializer, UserProfileSerializer, \
    RepairTypeSerializer, RepairSerializer,UserSerializer


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


class RepairTypeViewSet(viewsets.ModelViewSet):
    queryset = RepairType.objects.all()
    serializer_class = RepairTypeSerializer


class RepairViewSet(viewsets.ModelViewSet):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer
    filterset_fields = ['status']

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserView(UserDetailsView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        user_profile = user
        user_profile_data = UserSerializer(user_profile).data
        user_profile_data['id'] = user_profile.id
        return Response(user_profile_data)

    def update(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        user_data = dict()
        user_data['image'] = request.FILES['image']
        user_data['nameStudent'] = request.POST['nameStudent']
        user_data['student_id'] = request.POST['student_id']
        user_data['department'] = request.POST['department']
        user_data['branch'] = request.POST['branch']
        # user_data['nameRo'] = request.POST['nameRo']
        # user_data['room_type'] = request.POST['room_type']
        # user_data['domitory'] = request.POST['domitory']
        user_data['contact'] = request.POST['contact']
        user_data['face_book'] = request.POST['face_book']
        print(user_data)
        user_slz = UserSerializer(user, data=user_data)

        if user_slz.is_valid():
            user_slz.save()
        else:
            return Response(user_slz.error_messages, status=status.HTTP_400_BAD_REQUEST)

        profile = user
        try:
            profile.department_id = request.data.get("department")
            profile.branch_id = request.data.get("branch")
            profile.room_id = request.data.get("room")
            profile.phone = request.data.get("phone")
            profile.save()
            slz = serializers.UserProfileSerializer(profile)
            return Response(slz.data)
        except ValueError as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

