from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from offers.models import offers
# from users.models import User

class deals(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title= models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique_with='title')
    date_ajout =models.DateField(auto_now_add=True)
    good_deal= models.CharField(max_length=255)
    price_deal= models.IntegerField()
    offer=models.ForeignKey(offers,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='deal'
        verbose_name_plural='deals'


   