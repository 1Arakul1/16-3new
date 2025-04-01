from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название породы', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'

class Dog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Кличка')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='dogs', verbose_name='Порода')
    age = models.PositiveIntegerField(verbose_name='Возраст')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='dog_images/', blank=True, null=True, verbose_name='Фотография')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='dogs', verbose_name='Владелец')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'
