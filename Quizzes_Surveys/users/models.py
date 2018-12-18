from django.db import models
from django.contrib.auth.models import User
# from quiz.models import Quiz


class Teacher(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Prof {self.name.capitalize()}"


class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name.capitalize()}"


class Batch(models.Model):
    students = models.ManyToManyField(Student)
    teachers = models.ManyToManyField(Teacher)
    quizzes = models.ManyToManyField('quiz.Quiz')

    YEAR_CHOICES = (
        ("SE", "SE"),
        ("TE", "TE"),
        ("BE", "BE")
    )

    year = models.CharField(max_length=10, choices=YEAR_CHOICES, default="SE")

    DIVISION_CHOICES = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C")
    )

    division = models.CharField(max_length=10, choices=DIVISION_CHOICES, default="A")

    BATCH_CHOICES = {
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    }

    batch = models.CharField(max_length=10, choices=BATCH_CHOICES, default="1")

    def __str__(self):
        return f"{(str(self.year) + '-' + str(self.division) + str(self.batch)).upper()}"



