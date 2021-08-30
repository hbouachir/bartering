from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
# from users.models import User




# Create your models here.
class categories(models.Model):
    nom= models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='nom', unique=True)
   
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'


class offers(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title= models.CharField(max_length=255) #UNIQUE=True)
    slug = AutoSlugField(populate_from='title', unique_with='title')
    date_ajout =models.DateField(auto_now_add=True)
    barter_with= models.CharField(max_length=255)
    price= models.IntegerField()
    image = models.ImageField('image', upload_to='images/')
    categorie=models.ForeignKey(categories,null=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.title