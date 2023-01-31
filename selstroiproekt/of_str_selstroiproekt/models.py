from django.db import models
from django.urls import reverse


class Of_str_selstroiproekt(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m%d")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    """proekt = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)"""

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url (self) :
        return reverse ("post" ,kwargs = {"post_id" : self.pk})

    """class Category(models.Model):
        name = models.CharField(max_length=150,db_index=True)"""

     def __str__(self) :
         return self.name

    class Meta :
        verbose_name = "Производственный кооператив Институт Мозырьсельстройпроект"
        verbose_name_plural = "Производственный кооператив Институт Мозырьсельстройпроект"

