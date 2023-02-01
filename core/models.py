from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=150)
    join_date = models.DateField(auto_now=False, auto_now_add=False)
    salary = models.CharField(max_length=50)
    picture = models.ImageField(
        upload_to="profile_pic", null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
