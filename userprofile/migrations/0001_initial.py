# Generated by Django 3.0.8 on 2020-11-06 07:56

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
            name='UserProfileManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameManager', models.CharField(blank=True, max_length=255, null=True)),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
                ('rebuilding', models.CharField(blank=True, max_length=255, null=True)),
                ('contact', models.CharField(blank=True, max_length=10, null=True)),
                ('face_book', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='profile-images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameStudent', models.CharField(blank=True, max_length=255, null=True)),
                ('student_id', models.CharField(blank=True, max_length=8, null=True)),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('branch', models.CharField(blank=True, max_length=255, null=True)),
                ('contact', models.CharField(blank=True, max_length=10, null=True)),
                ('face_book', models.CharField(blank=True, max_length=255, null=True)),
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
                ('status', models.IntegerField(blank=True, choices=[(1, 'แจ้งซ่อม'), (2, 'รออนุมัติ'), (3, 'กำลังดำเนินงาน'), (4, 'ดำเนินการเสร็จสิ้น'), (5, 'ยกเลิกคำขอ')], null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('wait_date', models.DateField(blank=True, null=True)),
                ('approve_data', models.DateField(blank=True, null=True)),
                ('completed_data', models.DateField(blank=True, null=True)),
                ('imageBe', models.ImageField(blank=True, null=True, upload_to='imagesBe/')),
                ('imageAf', models.ImageField(blank=True, null=True, upload_to='imagesAf/')),
                ('note', models.TextField()),
                ('technician', models.TextField(blank=True, null=True)),
                ('repair_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.RepairType')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.Room')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
