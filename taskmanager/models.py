from django.db import models

# Create your models here.
class TaskManager(models.Model):
    done = 'd'
    pending = 'p'
    working = 'w'
    TASK_STATUS_CHOICES = (
        (done,'done'),
        (pending,'pending'),
        (working, 'working'),
    )
    title       = models.CharField(max_length=75)
    status      = models.CharField(max_length=1, choices=TASK_STATUS_CHOICES, default='done')
    description = models.TextField()
    
    def __str__(self):
        return str(self.title)