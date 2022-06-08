from django import forms

from .models import Exam

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
            'ecas', 'boards', 'notes')
