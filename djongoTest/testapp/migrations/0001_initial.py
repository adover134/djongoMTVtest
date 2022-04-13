# Generated by Django 4.0.3 on 2022-04-13 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('u_id', models.TextField(default='', primary_key=True, serialize=False)),
                ('u_name', models.TextField(default='홍길동')),
                ('u_email', models.EmailField(default='aaaaa@aaa.com', max_length=254)),
                ('inactivated_date', models.DateField(null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('u_id', models.OneToOneField(db_column='u_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='testapp.user')),
                ('m_tel', models.TextField(default='010-0101-1010')),
            ],
            options={
                'db_table': 'manager',
            },
        ),
    ]
