from django.db import models
from django.core.validators import URLValidator
from hashlib import sha1
from datetime import date
from django.utils.text import slugify

class Group(models.Model):
    group_name = models.CharField(max_length=50, help_text='Name of Event')
    event_date = models.DateField()
    pub_date = models.DateField(default=date.today)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.group_name)
        super(Group, self).save(*args, **kwargs)


class Gift(models.Model):
    title = models.CharField(max_length = 144)
    desc = models.TextField('description', blank=True, default='', help_text='Description of item')
    url = models.TextField(validators=[URLValidator()])
    only_one = models.BooleanField(default=True,help_text='When checked, only one of this item can be gifted.')

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
    
