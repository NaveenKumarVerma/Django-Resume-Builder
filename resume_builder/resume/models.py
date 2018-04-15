from __future__ import unicode_literals
from django.db import models


class Person(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def full_name(self):
        return " ".join([self.first_name, self.last_name])


class Education(models.Model):
    DEGREE_CHOICES = (
        ('Phd', 'Male'),
        ('Mtech/MA/MSc/MCom/MBA', 'Masters'),
        ('BE/Btech/BA/BSc/BCom', 'Masters'),
        ('12th', 'High School')
    )
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES)
    stream = models.CharField(max_length=100)
    passing_year = models.DateField()
    result = models.CharField(max_length=5)


class ProjectOrJob(models.Model):
    WORK_CHOICES = (
        ('J', 'Job'),
        ('P', 'Project')

    )

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    work = models.CharField(max_length=1, choices=WORK_CHOICES)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()


class ProfessionalSkills(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    skillDetail = models.TextField()


class Academics(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    academic_detail = models.TextField()


class AreaOfInterest(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    area_of_interest_detail = models.TextField()
