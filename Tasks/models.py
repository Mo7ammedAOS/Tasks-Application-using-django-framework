from django.db import models

# adding Task Feild

class Task(models.Model):
    added_task = models.CharField(max_length=50)
    check_task = models.BooleanField(default=False)


    def __str__(self):
        return self.added_task
