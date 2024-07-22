from django.db import models


class Posts(models.Model):
    title = models.CharField('Название', max_length=30)
    content = models.TextField('Содержание поста')

    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.content}"

    class Meta:  # даем название таблицы в админке
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Category(models.Model):
    name_category = models.CharField('Название категории', max_length=30)
    description_category = models.TextField('Короткое описание категории')

    def __str__(self):
        return f"{self.name_category} {self.description_category} "

    class Meta:  # даем название таблицы в админке
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
