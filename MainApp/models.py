from django.db import models


class Movies(models.Model):
    title = models.CharField("Название", max_length=100)
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
    film_ratings = models.FloatField("Рейтинг", default=0)
    link = models.CharField("Ссылка", max_length=100, blank=None)

    def __str__(self):
        return self.title
