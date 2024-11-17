# Generated by Django 5.1.3 on 2024-11-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rtype', models.CharField(choices=[('B', 'Beginning'), ('E', 'End')], max_length=1)),
                ('timestamp', models.DateTimeField()),
                ('call_id', models.BigIntegerField()),
                ('source', models.CharField(max_length=11, null=True)),
                ('destination', models.CharField(max_length=11, null=True)),
            ],
        ),
    ]
