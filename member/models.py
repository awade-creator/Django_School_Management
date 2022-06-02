from phone_field import PhoneField
from django.db import models


# Create your models here.


class Member(models.Model):
    user = models.OneToOneField('auth.User', null=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_primary = models.EmailField(max_length=50)
    email_secondary = models.EmailField(max_length=50, blank=True)
    primary_phone_number = PhoneField(blank=True, help_text='Contact phone number')
    secondary_phone_number = PhoneField(blank=True)
    medical_info = models.CharField(max_length=100)
    is_parent = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    dual_parent_student = models.BooleanField(default=False)
    age = models.IntegerField()
    male_gender = models.BooleanField(default=False)
    female_gender = models.BooleanField(default=False)
    guardian = models.BooleanField(default=False)
    notes = models.CharField(max_length=100)
    instructor = models.BooleanField(default=False)
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f'{self.user.username} Profile'
