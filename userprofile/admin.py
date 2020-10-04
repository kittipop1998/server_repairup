from django.contrib import admin
from .models import Dormitory, RoomType, Room, UserProfile, RepairType, Repair


# Register your models here.
class DormitoryAdmin(admin.ModelAdmin):
    pass


class RoomTypeAdmin(admin.ModelAdmin):
    pass


class RoomAdmin(admin.ModelAdmin):
    pass


class UserProfileAdmin(admin.ModelAdmin):
    pass


class RepairTypeAdmin(admin.ModelAdmin):
    pass


class RepairAdmin(admin.ModelAdmin):
    pass


admin.site.register(Dormitory, DormitoryAdmin)
admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(RepairType, RoomTypeAdmin)
admin.site.register(Repair, RepairAdmin)
