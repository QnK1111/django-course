# Generated by Django 5.0 on 2024-02-12 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_youtube',
            new_name='social_website',
        ),
    ]
