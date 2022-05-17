from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TKD_CHOICES = [
    ('BLANK', 'N/A'),
    ('TIGER CUB', 'Tiger Cub'),
    ('JR', 'Jr'), ('YOUTH', 'Youth'),
    ('ADULT', 'Adult')
]

XP_CHOICES = [
    ('BLANK', 'N/A'),
    ('BEGINNER', 'Beginner'),
    ('INTERMEDIATE', 'Intermediate'),
    ('ADVANCED', 'Advanced')
]

SC_CHOICES = [
    ('BLANK', 'N/A'),
    ('WHITE', 'White'),
    ('YELLOW', 'Yellow')
]


class Profile(models.Model):
    user = models.OneToOneField('auth.User', null=True, on_delete=models.SET_NULL)
    parent = models.BooleanField()
    student = models.BooleanField()
    dual_parent_student = models.BooleanField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_primary = models.CharField(max_length=50)
    email_secondary = models.CharField(max_length=50)
    mobile_one = models.IntegerField()
    mobile_two = models.IntegerField()
    phone_one = models.IntegerField()
    age = models.CharField(max_length=3)
    gender = models.BooleanField()
    guardian = models.CharField(max_length=50)
    notes = models.CharField(max_length=100)
    medical_info = models.CharField(max_length=100)
    rank = models.CharField(max_length=50)
    tkd_program = models.CharField(max_length=200, choices=TKD_CHOICES)
    xp_program = models.CharField(max_length=100, choices=XP_CHOICES)
    sc_program = models.CharField(max_length=100, choices=SC_CHOICES)
    instructor = models.BooleanField()
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f'{self.user.username} Profile'
