<<<<<<< HEAD
# Generated by Django 3.0.8 on 2020-10-24 05:36
=======
# Generated by Django 2.2.3 on 2020-10-24 05:09
>>>>>>> 6c0ad7558fe0d96cb05e89e589009f96780a06d5

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dormitory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameDo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RepairType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameRe', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameRo', models.CharField(max_length=255)),
                ('dormitory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.Dormitory')),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameTy', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameStudent', models.CharField(max_length=255)),
                ('student_id', models.CharField(max_length=8)),
                ('department', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=10)),
                ('face_book', models.CharField(max_length=255)),
                ('image', models.FileField(blank=True, null=True, upload_to='profile-images/')),
                ('dormitory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.Dormitory')),
                ('nameRo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.Room')),
                ('room_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.RoomType')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.RoomType'),
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.TextField()),
                ('desc', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('status', models.IntegerField(blank=True, choices=[(1, 'แจ้งซ่อม'), (2, 'กำลังดำเนินงาน'), (3, 'ดำเนินการเสร็จสิ้น'), (4, 'ยกเลิกคำขอ')], null=True)),
<<<<<<< HEAD
                ('completed_data', models.DateField(blank=True, null=True)),
                ('approve_data', models.DateField(blank=True, null=True)),
=======
                ('completed_data', models.DateField()),
                ('approve_data', models.DateField()),
>>>>>>> 6c0ad7558fe0d96cb05e89e589009f96780a06d5
                ('imageBe', models.ImageField(blank=True, null=True, upload_to='imagesBe/')),
                ('imageAf', models.ImageField(blank=True, null=True, upload_to='imagesAf/')),
                ('repair_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.RepairType')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.Room')),
<<<<<<< HEAD
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.UserProfile')),
=======
>>>>>>> 6c0ad7558fe0d96cb05e89e589009f96780a06d5
            ],
        ),
    ]
