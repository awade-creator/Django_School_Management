import datetime

from django import forms
from django.forms import ModelForm
from student.models import Student, Exam

RESULT = [
    ('', ''),
    (0, 'FAIL'),
    (1, 'PASS'),
]

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

EXAM_TIER = [
    ('', ''),
    ('Leveled-White', 'Leveled-White'),
    ('Leveled-Yellow', 'Leveled-Yellow'),
    ('Leveled-Green', 'Leveled-Green'),
    ('Leveled-Blue', 'Leveled-Blue'),
    ('Leveled-Brown', 'Leveled-Brown'),
    ('Leveled-Red', 'Leveled-Red'),
    ('Elevated *', 'Elevated *'),
    ('Elevated **', 'Elevated **'),
    ('Elevated ***', 'Elevated ***')
]


class ExamCreateForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = (
            'form_cadence',
            'contact',
            'one_step',
            'sparring',
            'ecas',
            'boards',
            'notes'
        )


"""


class ExamCreateForm(ModelForm):
    exam_title = forms.ChoiceField(choices=EXAM_SELECTION)
    current_rank = forms.ChoiceField(label='Current Rank', choices=EXAM_TIER)
    form_cadence = forms.ChoiceField(label='Form ', choices=RESULT)
    contact = forms.ChoiceField(label='Contacts', choices=RESULT)
    one_step = forms.ChoiceField(label='One Steps', choices=RESULT)
    sparring = forms.ChoiceField(label='Sparring', choices=RESULT)
    ecas = forms.ChoiceField(label='ECAS', choices=RESULT)
    boards = forms.ChoiceField(label='Board Breaks', choices=RESULT)
    results = forms.CharField()
    exam_author = forms.CharField(label='Exam Author')  # Get Current_User for Author
    notes = forms.CharField()
"""
