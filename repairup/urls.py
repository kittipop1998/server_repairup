"""repairup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from userprofile import views as userprofile_views
from django.conf.urls import url

router = routers.SimpleRouter()

router.register('Dormitorys', userprofile_views.DormitoryViewSet)
router.register('RoomTypes', userprofile_views.RoomTypeViewSet)
router.register('Rooms', userprofile_views.RoomViewSet)
router.register('UserProfiles', userprofile_views.UserProfileViewSet)
# router.register('Registers', userprofile_views.UserRegisterView)
router.register('RepairType', userprofile_views.RepairTypeViewSet)
router.register('Repairs', userprofile_views.RepairViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/user-profile/', userprofile_views.UserView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

