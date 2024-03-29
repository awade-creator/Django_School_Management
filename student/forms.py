from django import forms

from .models import Exam, Student

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


class StudentExamCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name',
                  'last_name',
                  'age',
                  'rank',
                  'tkd_program',
                  'xp_program',
                  'sc_program',
                  'instructor')
