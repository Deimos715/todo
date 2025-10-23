from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    '''
    Модель задачи TODO: хранит название, подробное описание, владельца,
    статус выполнения и автоматически выставляемые даты создания и обновления.
    '''

    title = models.CharField(max_length=100, verbose_name='Название')
    memo = models.TextField(blank=True, verbose_name='Описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')

    completed = models.BooleanField(default=False, verbose_name='Завершена')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлена')

    def __str__(self):
        return self.title
