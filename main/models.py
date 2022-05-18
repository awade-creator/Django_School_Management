from django.db import models


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField('auth.User', null=True, on_delete=models.SET_NULL)
    username = models.CharField(max_length=16)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_primary = models.CharField(max_length=50)
    email_secondary = models.CharField(max_length=50)
    mobile_one = models.IntegerField()
    mobile_two = models.IntegerField()
    phone_one = models.IntegerField()
    medical_info = models.CharField(max_length=100)
    parent = models.BooleanField()
    student = models.BooleanField()
    dual_parent_student = models.BooleanField()
    age = models.CharField(max_length=3)
    gender = models.BooleanField()
    guardian = models.CharField(max_length=50)
    notes = models.CharField(max_length=100)
    instructor = models.BooleanField()
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f'{self.user.username} Profile'
