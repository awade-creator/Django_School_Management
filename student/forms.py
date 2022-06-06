from django import forms

from .models import Exam

RESULT = [
    ('', ''),
    (0, 'FAIL'),
    (1, 'PASS'),
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
            'exam_title', 'form_cadence', 'contact', 'one_step', 'sparring',
            'ecas', 'boards', 'notes', 'results')


"""
        widgets = {
            'exam_title'  : forms.Select(attrs={'class': 'form-control'}),
            'form_cadence': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'contact'     : forms.CheckboxInput(attrs={'class': 'form-control'}),
            'one_step'    : forms.CheckboxInput(attrs={'class': 'form-control'}),
            'sparring'    : forms.CheckboxInput(attrs={'class': 'form-control'}),
            'ecas'        : forms.CheckboxInput(attrs={'class': 'form-control'}),
            'boards'      : forms.CheckboxInput(attrs={'class': 'form-control'}),
            'notes'       : forms.TextInput(attrs={'class': 'form-control'}),
        }
"""
