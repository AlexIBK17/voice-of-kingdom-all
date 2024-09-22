# Generated by Django 4.2.13 on 2024-09-22 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_contactsubmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Contact Submission',
                'verbose_name_plural': 'Contact Submissions',
                'ordering': ['-submitted_at'],
            },
        ),
        migrations.DeleteModel(
            name='ContactSubmission',
        ),
    ]
