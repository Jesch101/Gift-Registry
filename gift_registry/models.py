from django.db import models
from django.core.validators import URLValidator
from hashlib import sha1
from datetime import date
from django.utils.text import slugify
from django.urls import reverse

class Group(models.Model):
    event_name = models.CharField(max_length=50)
    event_date = models.DateField()
    join_code = models.CharField(max_length=15)
    pub_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=False)
    
    def __str__(self):
        return self.event_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.event_name)
        super(Group, self).save(*args, **kwargs)


class Gift(models.Model):
    group = models.ForeignKey(Group, related_name='gift', on_delete=models.CASCADE)
    title = models.CharField(max_length = 144)
    desc = models.TextField('description', blank=True, default='')
    url = models.TextField(validators=[URLValidator()])
    only_one = models.BooleanField(default=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        super(Gift, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Gifter(models.Model):  
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    # email = models.EmailField()

    class Meta:
        ordering = ['id']
        unique_together = ('gift', 'name')

    def __str__(self):
        return self.name
    
