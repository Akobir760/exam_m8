from django.db import models

# from .staff_model import Organization
# from .group_models import Group
# from .auth_user import AccountModel

class Course(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    user = models.ForeignKey("configapp.AccountModel", on_delete=models.CASCADE)
    descriptions = models.CharField(max_length=500, null=True, blank=True)
    is_staff = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=True)


    def __str__(self):
        return self.full_name


class Student(models.Model):
    user = models.ForeignKey("configapp.AccountModel", on_delete=models.CASCADE)
    # organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    is_activate = models.BooleanField(default=False)
    group = models.ManyToManyField("configapp.Group",related_name='group')
    descriptions = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.full_name

