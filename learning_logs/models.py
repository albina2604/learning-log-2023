from django.db import models

# Create your models here.


class Topic(models.Model):
    """Тема, що вивчає користувач"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Повертає символьне представлення моделі"""
        return self.text
