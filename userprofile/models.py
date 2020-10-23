from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User

# User = get_user_model()


class Dormitory(models.Model):
    nameDo = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.nameDo)


class RoomType(models.Model):
    nameTy = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.nameTy)


class Room(models.Model):
    nameRo = models.CharField(max_length=255)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True, blank=True)
    dormitory = models.ForeignKey(Dormitory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.dormitory, self.nameRo)


class UserProfile(User):
    nameUs = models.CharField(max_length=255)
    # yearUs = models.CharField(max_length=4)
    department = models.TextField()
    branch = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    # room_type = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    # dormitory = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    # phone = models.CharField(max_length=255)
    # facebook = models.CharField(max_lenth=100)
    # image = models.FileField(upload_to='image_uer/', null=True, blank=True)


    def __str__(self):
        return "{}".format(self.nameUs)


class RepairType(models.Model):
    nameRe = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.nameRe)


class Repair(models.Model):
    status_choices = [
        (1, 'แจ้งซ่อม'),
        (2, 'กำลังดำเนินงาน'),
        (3, 'ดำเนินการเสร็จสิ้น'),
        (4, 'ยกเลิกคำขอ')
    ]

    contact = models.TextField()
    desc = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(null=True, blank=True, choices=status_choices)
    completed_data = models.DateField()
    approve_data = models.DateField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    aftermage = models.ImageField(upload_to='images/', null=True, blank=True)
    user_profile = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.SET_NULL)
    repair_type = models.ForeignKey(RepairType, on_delete=models.SET_NULL, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.desc, self.repair_type)
