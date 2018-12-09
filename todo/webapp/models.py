from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=75, null=False, blank=False, verbose_name='Название')
    status = models.CharField(max_length=30, null=False, blank=False, default='new', verbose_name='Статус')

    def __str__(self):
        return f' {self.pk}. {self.name} ({self.status})'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

