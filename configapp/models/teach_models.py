from django.db import models


from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.hashers import make_password, check_password

class OTPCode(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_time = models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expire_time

    def __str__(self):
        return f"{self.email} - {self.code}"


class Course(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    username = models.CharField(max_length=255, unique=True, default="test_user")
    full_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(default=123)
    descriptions = models.CharField(max_length=500, null=True, blank=True)
    is_staff = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=True)
    otp = models.CharField(blank=True, null=True)
    group = models.ManyToManyField('configapp.Group', related_name='teachers', blank=True)


    def __str__(self):
        return self.full_name
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


class Student(models.Model):
    username = models.CharField(max_length=255, unique=True, default="test_user")
    full_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    passwords = models.CharField(default=123)
    is_activate = models.CharField(default="activmas")
    descriptions = models.CharField(max_length=500, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    otp = models.CharField(blank=True, null=True)
    s_group = models.ManyToManyField('configapp.Group', related_name='students', blank=True)
    created = models.DateField(default="2025-09-14")
    updated = models.DateTimeField(default="2025-09-14")

    def __str__(self):
        return self.full_name
    
    def set_password(self, raw_password):
        self.passwords = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.passwords)

class Exam(models.Model):
    title = models.CharField(max_length=100)
    group = models.ForeignKey("configapp.Group", on_delete=models.CASCADE, related_name='exams')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='exams')
    date = models.DateField()

    passed_students = models.ManyToManyField(Student, related_name='passed_exams', blank=True)
    failed_students = models.ManyToManyField(Student, related_name='failed_exams', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.group})"
