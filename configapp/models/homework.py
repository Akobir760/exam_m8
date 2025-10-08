from django.db import models
from configapp.models.teach_models import Student, Teacher
from configapp.models.group_models import Group



class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="subjects"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Homework(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="homeworks")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="homeworks")
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name="given_homeworks")
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.group.name})"


class HomeworkSubmission(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="submissions")
    submitted_at = models.DateTimeField(auto_now_add=True)
    text_answer = models.TextField(blank=True, null=True)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username()} - {self.homework.title}"


class HomeworkReview(models.Model):
    submission = models.OneToOneField(HomeworkSubmission, on_delete=models.CASCADE, related_name="review")
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name="reviews")
    grade = models.PositiveIntegerField(default=0)
    comment = models.TextField(blank=True, null=True)
    reviewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.submission.student.username()} ({self.submission.homework.title})"
