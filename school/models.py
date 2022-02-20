from django.db import models

class Student(models.Model):
    STATUS = (
        ('activate', 'Activate'),
        ('not activate', 'Not Activate')
    )
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=False, max_length=30)
    rg = models.CharField(max_length=9, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField()
    cell_phone = models.CharField(max_length=14)
    status = models.CharField(max_length=12, choices=STATUS, blank=False, null=False,default='activate')

    def __str__(self):
        return self.name

class Course(models.Model):
    LEVEL = (
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    )
    course_code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=100)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, null=False,default='B')

    def __str__(self):
        return self.description

class Enrollment(models.Model):
    PERIOD = (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('N', 'Night')
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(max_length=1, choices=PERIOD, blank=False, null=False,default='M')


