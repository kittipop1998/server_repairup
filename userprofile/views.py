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
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status

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
        user_profile = UserProfile.objects.get(user=user)
        request_data = request.data
        print(request_data['nameStudent'])
        user_data = dict()
        try :
            user_profile.image = request.FILES['image']
        except :
            pass
        try:
            user_profile.nameRo = request_data['nameRo']
        except:
            pass
        try:
            user_profile.room_type = request_data['room_type']
        except:
            pass
        try:
            user_profile.domitory = request_data['domitory']
        except:
            pass
        try:
            user_profile.nameStudent = request_data['nameStudent']
        except:
            pass
        try:
            user_profile.student_id = request_data['student_id']
        except:
            pass
        try:
            user_profile.department = request_data['department']
        except:
            pass
        try:
            user_profile.branch = request_data['branch']
        except:
            pass
        try:
            user_profile.contact = request_data['contact']
        except:
            pass
        try:
            user_profile.face_book = request_data['face_book']
        except:
            pass

        # user_data['student_id'] = request.POST['student_id']
        # user_data['department'] = request.POST['department']
        # user_data['branch'] = request.POST['branch']
        # user_data['contact'] = request.POST['contact']
        # user_data['face_book'] = request.POST['face_book']
        user_profile.save()

        return  Response(UserProfileSerializer(user_profile).data)




class Register(APIView):
    def post(self, request):
      user = User.objects.create(
                username=request.data.get('username'),
                email=request.data.get('email'),
                first_name=request.data.get('first_name'),
                last_name=request.data.get('last_name'),
                is_staff = request.data.get('is_staff'),
                # is_superuser = request.data.get('is_superuser'),
            )
      user.set_password(str(request.data.get('password')))
      user.save()
      return Response({"status":"success","response":"User Successfully Created"}, status=status.HTTP_201_CREATED)


class MyRepair(APIView):
    def get(self, request, pk):

        items = Repair.objects.filter(user=pk).order_by('pk')
        try:
            req_data = int(request.GET['status'])
            items = items.filter(status=req_data)
        except :
            pass
        serializer = RepairSerializer(items, many=True)
        return Response(serializer.data)