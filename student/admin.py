from django.contrib import admin
from .models import Student


# Register your models here.

class Students(admin.ModelAdmin):
    fields = [
        'first_name',
        'last_name',
        'age',
        'rank',
        'tkd_program',
        'xp_program',
        'sc_program',
        'instructor',
        'updated'
    ]

    admin.site.register(Student)
