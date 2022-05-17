from django.db import models

# Choices used for model Student


RANK_CHOICES = [
    ('BLANK', 'N/A'),
    ('CUB_WHITE', 'Cub_White'),
    ('CUB_YELLOW', 'Cub_Yellow'),
    ('CUB_GREEN', 'Cub_Green'),
    ('CUB_BLUE', 'Cub_Blue'),
    ('CUB_BROWN', 'Cub_Brown'),
    ('CUB_RED', 'Cub_Red'),
    ('CUB_BLACK', 'Cub_Black'),
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
    ('BLACK_1ST_1', 'Black_1ST_1'),
    ('BLACK_1ST_2', 'Black_1ST_2'),
    ('BLACK_1ST_3', 'Black_1ST_3'),
    ('BLACK_2ND_1', 'Black_2ND_1'),
    ('BLACK_2ND_2', 'Black_2ND_2'),
    ('BLACK_2ND_3', 'Black_2ND_3'),
    ('BLACK_3RD_1', 'Black_3RD_1'),
    ('BLACK_3RD_2', 'Black_3RD_2'),
    ('BLACK_3RD_3', 'Black_3RD_3'),
    ('BLACK_4TH_1', 'Black_4TH_1'),
    ('BLACK_4TH_2', 'Black_4TH_2'),
    ('BLACK_4TH_3', 'Black_4TH_3'),
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
    updated = models.DateTimeField(auto_created=True)
