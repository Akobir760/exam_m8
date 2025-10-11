from django.db import models
# from configapp.models.teach_models import Teacher
# from configapp.models.group_models import Group


class TableTypeModel(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class TableModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    table_type = models.ForeignKey(TableTypeModel, on_delete=models.CASCADE, related_name='tables')
    teacher = models.ForeignKey("configapp.Teacher", on_delete=models.CASCADE, related_name='tables')
    group = models.ForeignKey("configapp.Group", on_delete=models.CASCADE, related_name='tables')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.group})"
