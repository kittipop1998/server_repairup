<<<<<<< HEAD
# Generated by Django 2.2.3 on 2020-10-23 05:53

=======
<<<<<<< HEAD
# Generated by Django 3.0.8 on 2020-10-22 09:46

=======
<<<<<<< HEAD
# Generated by Django 2.2.3 on 2020-10-22 07:53

=======
>>>>>>> f887b3886e831140a1325f00f93e54dd779fd9a6
>>>>>>> 1738b4468f4dbc6b9974bcc0daffe6c5131b611b
>>>>>>> b752938c6f771808ba989f0a100f372a380ceb2d
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
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
                ('completed_data', models.DateField()),
                ('approve_data', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('afterimage', models.ImageField(blank=True, null=True, upload_to='images/')),
=======
                ('request_date', models.DateField(auto_now=True)),
                ('completed_data', models.DateField(auto_now=True)),
                ('approve_data', models.DateField(auto_now=True)),
                ('imageBe', models.ImageField(blank=True, null=True, upload_to='imagesBe/')),
                ('imageAf', models.ImageField(blank=True, null=True, upload_to='imagesAf/')),
>>>>>>> 1738b4468f4dbc6b9974bcc0daffe6c5131b611b
                ('repair_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.RepairType')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.Room')),
            ],
        ),
    ]
