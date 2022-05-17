import datetime

from django import forms

from exam.models import Exam

RESULT = [
    ('0', ''),
    ('PASS', 'Pass'),
    ('FAIL', 'Fail')
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
        fields = ['exam_title',
                  'first_name',
                  'last_name',
                  'rank',
                  'form_cadence',
                  'contact',
                  'one_step',
                  'sparring',
                  'ecas',
                  'boards',
                  'exam_author',
                  'notes',
                  ]


class RawExamCreateForm(forms.Form):
    exam_title = forms.ChoiceField(choices=EXAM_SELECTION)
    current_rank = forms.ChoiceField(label='Current Rank', choices=EXAM_TIER,
                                     widget=forms.Select(
                                         attrs={'class': 'form-control form-control-sm, dropdown, col-md-6, row g-3'}))
    form_cadence = forms.ChoiceField(label='Form ', choices=RESULT,
                                     widget=forms.Select(
                                         attrs={'class': 'form-control form-control-sm, dropdown, col-md-6, row g-3'}))
    contact = forms.ChoiceField(label='Contacts', choices=RESULT,
                                widget=forms.Select(attrs={'class': 'dropdown, col-md-6, row g-3'}))
    one_step = forms.ChoiceField(label='One Steps', choices=RESULT,
                                 widget=forms.Select(attrs={'class': 'dropdown, col-md-6, row g-3'}))
    sparring = forms.ChoiceField(label='Sparring', choices=RESULT,
                                 widget=forms.Select(attrs={'class': 'dropdown, col-md-6, row g-3'}))
    ecas = forms.ChoiceField(label='ECAS', choices=RESULT,
                             widget=forms.Select(attrs={'class': 'dropdown, col-md-6, row g-3'}))
    boards = forms.ChoiceField(label='Board Breaks', choices=RESULT,
                               widget=forms.Select(attrs={'class': 'dropdown, col-md-6, row g-3'}))
    results = forms.CharField()
    exam_author = forms.CharField(label='Exam Author')  # Get Current_User for Author
    notes = forms.CharField(required=False, label='Notes', widget=forms.Textarea(attrs={'rows': 3}))
