# Generated by Django 3.2.5 on 2021-07-06 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210706_0932'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['student_name']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(db_index=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(blank=True, choices=[('study', 'Учится'), ('deducted', 'Отчислен'), ('work', 'Работает'), ('fired', 'Уволен')], default='s', help_text='статус ученика', max_length=50),
        ),
    ]
