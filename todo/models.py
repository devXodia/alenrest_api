from django.db import models
from django.conf import settings
import datetime
from django.contrib.auth.models import User
from datetime import date

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def time_passed(self):
        current = date.today()
        sum = current - self.created_at

        return sum.days
