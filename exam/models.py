from django.db import models
from django.urls import reverse


# Create your models here.


class Exam(models.Model):
    exam_title = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
    form_cadence = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    one_step = models.CharField(max_length=20)
    sparring = models.CharField(max_length=20)
    ecas = models.CharField(max_length=20)
    boards = models.CharField(max_length=20)
    results = models.CharField(max_length=20)
    exam_author = models.CharField(max_length=50)
    notes = models.CharField(max_length=250)
    updated = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('/exam_detail/', kwargs={'slug': self.slug})
