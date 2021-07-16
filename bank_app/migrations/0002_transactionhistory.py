# Generated by Django 3.2.3 on 2021-07-08 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_id', models.IntegerField()),
                ('sender_name', models.CharField(max_length=100)),
                ('receiver_id', models.IntegerField()),
                ('receiver_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]