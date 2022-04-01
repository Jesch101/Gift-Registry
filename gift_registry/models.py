from django.db import models
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

    def get_absolute_url(self):
        return reverse("group_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.event_name)
        super(Group, self).save(*args, **kwargs)

class Gift(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length = 144)
    reciever = models.CharField(max_length = 50, blank=False, default='')
    desc = models.TextField('description', blank=True, default='')
    url = models.URLField(max_length=200)
    only_one = models.BooleanField(default=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        super(Gift, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Gifter(models.Model):  
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE, default='')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default ='')
    name = models.CharField(max_length=55)

    class Meta:
        ordering = ['id']
        unique_together = ('group', 'name')

    def __str__(self):
        return self.name
    
