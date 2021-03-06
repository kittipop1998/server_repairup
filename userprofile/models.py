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


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nameStudent = models.CharField(max_length=255, null=True, blank=True)
    student_id = models.CharField(max_length=8, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    rebuilding = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    branch = models.CharField(max_length=255, null=True, blank=True)
    nameRo = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True, blank=True)
    dormitory = models.ForeignKey(Dormitory, on_delete=models.SET_NULL, null=True, blank=True)
    contact = models.CharField(max_length=10, null=True, blank=True)
    face_book = models.CharField(max_length=255, null=True, blank=True)
    image = models.FileField(upload_to='profile-images/', null=True, blank=True)

    def __str__(self):
        return "{}".format(self.nameStudent)

class UserProfileManager(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        nameManager = models.CharField(max_length=255, null=True, blank=True)
        position = models.CharField(max_length=255, null=True, blank=True)
        rebuilding = models.CharField(max_length=255, null=True, blank=True)
        contact = models.CharField(max_length=10, null=True, blank=True)
        face_book = models.CharField(max_length=255, null=True, blank=True)
        image = models.FileField(upload_to='profile-images/', null=True, blank=True)

        def __str__(self):
            return "{}".format(self.nameManager)


class RepairType(models.Model):
    nameRe = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.nameRe)


class Repair(models.Model):
    status_choices = [
        (1, 'แจ้งซ่อม'),
        (2, 'รออนุมัติ'),
        (3, 'กำลังดำเนินงาน'),
        (4, 'ดำเนินการเสร็จสิ้น'),
        (5, 'ยกเลิกคำขอ'),

    ]

    contact = models.TextField()
    desc = models.TextField()
    status = models.IntegerField(null=True, blank=True, choices=status_choices)
    created_date = models.DateField(auto_now_add=True)
    wait_date = models.DateField(null=True, blank=True)
    approve_data = models.DateField(null=True, blank=True)
    completed_data = models.DateField(null=True, blank=True)
    imageBe = models.ImageField(upload_to='imagesBe/', null=True, blank=True)
    imageAf = models.ImageField(upload_to='imagesAf/', null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    repair_type = models.ForeignKey(RepairType, on_delete=models.SET_NULL, null=True, blank=True)
    note = models.TextField()
    technician = models.TextField(null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.desc, self.repair_type)
