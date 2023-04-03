from django.db import models
from accounts.models import Student, University

# Create your models here.
STATUS = (
    ("Waiting", "Waiting"),
    ("Shortlisted", "Shortlisted"),
    ("Accepted", "Accepted"),
)


class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    applied_date = models.DateField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default="Waiting", max_length=50)

    def __str__(self):
        return str(f'{self.id}')
