from django.db import models


# Create your models here.
class Events(models.Model):
    title = models.CharField('Событие', max_length=50)
    full_text = models.TextField('Описание')
    date = models.DateField('Дата события')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/events/{self.id}'


    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"