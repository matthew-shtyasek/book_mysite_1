from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='p')


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique_for_date='publish')  # unique_for_date - добавить дату из поля к адресу
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')  # TODO:посмотреть related_name
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)  # timezone - утилита Django
    created = models.DateTimeField(auto_now_add=True)  # дата автоматически сохраняется при создании объекта
    updated = models.DateTimeField(auto_now=True)  # дата автоматически сохраняется при сохранении объекта
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')

    objects = models.Manager()  # менеджер по умолчанию
    published = PublishedManager()  # наш менеджер
    # primary_key=True сделает поле первичным ключом, иначе Django создаст это поле автоматически

    class Meta:
        ordering = ('-publish', )  # инвертированная сортировка по полю publish
        # db_table позволяет переопределить название таблицы (так оно формируется из appname_modelname)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.publish.year, self.publish.month,
                                                 self.publish.day, self.slug))
