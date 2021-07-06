# Generated by Django 3.2.5 on 2021-07-06 05:33

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
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_of_user', models.CharField(db_index=True, max_length=100)),
                ('department_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(db_index=True, max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('place_of_study', models.CharField(db_index=True, max_length=200)),
                ('faculty', models.CharField(db_index=True, max_length=200)),
                ('status', models.CharField(blank=True, choices=[('s', 'Учится'), ('n', 'Отчислен'), ('w', 'Работает'), ('nw', 'Уволен')], default='s', help_text='статус ученика', max_length=2)),
                ('summary', models.CharField(db_index=True, max_length=1000)),
                ('begin_of_study', models.DateField(blank=True, null=True)),
                ('department_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.department')),
                ('mentor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(db_index=True, max_length=200)),
                ('mentor_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('student_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.student')),
            ],
        ),
    ]