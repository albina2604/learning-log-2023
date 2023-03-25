from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    """Тема, що вивчає користувач"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Повертає символьне представлення моделі"""
        return self.text


class Entry(models.Model):
    """Інформація, що вивчив користувач за темою"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Повертає символьне представлення моделі"""
        return f'{self.text[:50]}...'
