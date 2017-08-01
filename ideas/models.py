# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
from django.utils import timezone
from django.utils.text import slugify


class PublushedManager(models.Manager):
    def get_queryset(self):
        return super(PublushedManager,self).get_queryset().filter(status='published')


class Ideas(models.Model):
    TYPES_IDEA = (
        ('música', 'Música'),
        ('arte', 'Arte'),
        ('tecnologia', 'Tecnología'),
        ('derecho', 'Derecho'),
        ('medioAmbiente', 'Medio Ambiente'),
        ('otro', 'Otros'),)

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='ideas_created')
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    type = models.CharField(max_length=15, choices=TYPES_IDEA)
    slug = models.SlugField(max_length=200,
                            blank=True)
    user_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='ideas_like', blank=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    objects = models.Manager()
    published = PublushedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super(Ideas, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ideas:detail', args=[self.pk, self.slug])