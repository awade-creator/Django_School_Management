from django.db import models

# Choices used for model Student
from django.db.models import ManyToManyField

from member.models import Member

EXAM_SELECTION = [
    ('', ''),
    ('HO-AM', 'HO-AM'),
    ('Seed Form', 'Seed Form'),
    ('Plant Form', 'Plant Form'),
    ('Water Form', 'Water Form'),
    ('Sun Form', 'Sun Form'),
    ('Earth Form', 'Earth Form'),
    ('Fire Form', 'Fire Form'),
    ('Sky Form', 'Sky Form'),
    ('Tiger Form', 'Tiger Form'),
    ('Oak Form', 'Oak Form'),
    ('Eagle Form', 'Eagle Form'),
    ('Ocean Form', 'Ocean Form'),
    ('River Form', 'River Form'),
    ('Bear Form', 'Bear Form'),
    ('Mountain Form', 'Mountain Form')
]

RANK_CHOICES = [
    ('BLANK', 'N/A'),
    ('CUB_WHITE', 'Cub_White'),
    ('CUB_YELLOW', 'Cub_Yellow'),
    ('CUB_GREEN', 'Cub_Green'),
    ('CUB_BLUE', 'Cub_Blue'),
    ('CUB_BROWN', 'Cub_Brown'),
    ('CUB_RED', 'Cub_Red'),
    ('CUB_BLACK', 'Cub_Black'),
    ('CUB_GRADUATE', 'Cub_Graduate'),
    ('WHITE', 'White'),
    ('YELLOW', 'Yellow'),
    ('GREEN_1', 'Green_1'),
    ('GREEN_2', 'Green_2'),
    ('GREEN_3', 'Green_3'),
    ('BLUE_1', 'Blue_1'),
    ('BLUE_2', 'Blue_2'),
    ('BLUE_3', 'Blue_3'),
    ('BROWN_1', 'Brown_1'),
    ('BROWN_2', 'Brown_2'),
    ('BROWN', 'Brown_3'),
    ('RED_1', 'Red_1'),
    ('RED_2', 'Red_2'),
    ('RED_3', 'Red_3'),
    ('PROBATIONARY_BLACK', 'Probationary_Black'),
    ('PROBATIONARY_BLACK_1ST', 'Probationary_Black_1ST'),
    ('PROBATIONARY_BLACK_2ND', 'Probationary_Black_2ND'),
    ('PROBATIONARY_BLACK_3RD', 'Probationary_Black_3RD'),
    ('PROBATIONARY_BLACK_4TH', 'Probationary_Black_4TH'),
    ('BLACK_1ST_L1', 'Black_1ST_L1'),
    ('BLACK_1ST_L2', 'Black_1ST_L2'),
    ('BLACK_1ST_L3', 'Black_1ST_L3'),
    ('BLACK_1ST_L4', 'Black_1ST_L4'),
    ('BLACK_2ND_L1', 'Black_2ND_L1'),
    ('BLACK_2ND_L2', 'Black_2ND_L2'),
    ('BLACK_2ND_L3', 'Black_2ND_L3'),
    ('BLACK_2ND_L4', 'Black_2ND_L4'),
    ('BLACK_3RD_L1', 'Black_3RD_L1'),
    ('BLACK_3RD_L2', 'Black_3RD_L2'),
    ('BLACK_3RD_L3', 'Black_3RD_L3'),
    ('BLACK_3RD_L4', 'Black_3RD_L4'),
    ('BLACK_4TH_L1', 'Black_4TH_L1'),
    ('BLACK_4TH_L2', 'Black_4TH_L2'),
    ('BLACK_4TH_L3', 'Black_4TH_L3'),
    ('SR_1ST_DEGREE', 'Sr_1st_Degree'),
    ('SR_2ND_DEGREE', 'Sr_2nd_Degree'),
    ('SR_3RD_DEGREE', 'Sr_3rd_Degree'),
    ('SR_4TH_DEGREE', 'Sr_4th_Degree')
]

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

INSRTUCTOR_CHOICES = [
    ('BLANK', 'N/A'),
    ('LEADERSHIP', 'Leadership'),
    ('ASSISTANT', 'Assistant'),
    ('HONORS', 'Honors'),
]


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    rank = models.CharField(max_length=200, choices=RANK_CHOICES)
    tkd_program = models.CharField(max_length=200, choices=TKD_CHOICES)
    xp_program = models.CharField(max_length=100, choices=XP_CHOICES)
    sc_program = models.CharField(max_length=100, choices=SC_CHOICES)
    instructor = models.BooleanField()
    instructor_level = models.CharField(max_length=100, choices=INSRTUCTOR_CHOICES, default='N/A')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.last_name + ', ' + self.first_name


class Exam(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam_title = models.CharField(max_length=20, choices=EXAM_SELECTION, blank=True)
    form_cadence = models.BooleanField(default=False)
    contact = models.BooleanField(default=False)
    one_step = models.BooleanField(default=False)
    sparring = models.BooleanField(default=False)
    ecas = models.BooleanField(default=False)
    boards = models.BooleanField(default=False)
    results = models.CharField(max_length=20, blank=True)
    exam_author = models.CharField(max_length=50, blank=True)
    notes = models.CharField(max_length=250, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.exam_title)
