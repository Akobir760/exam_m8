from django.db import models



class AttendanceLevel(models.Model):

    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title


class Attendance(models.Model):
    level = models.ForeignKey(AttendanceLevel, on_delete=models.RESTRICT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    student = models.ForeignKey("configapp.Student", on_delete=models.RESTRICT)
    group = models.ForeignKey("configapp.Group", on_delete=models.RESTRICT)

    def __str__(self):
        return self.level
