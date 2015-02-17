from django.db import models

from django.db.models.signals import post_delete
from django.dispatch import receiver





class Category(models.Model):
	#Categorias de fotos
	name = models.CharField(max_length=50)
	def __unicode__(self):
		return self.name

class Photo(models.Model):
	#Fotos del album
	categori = models.ForeignKey(Category,null=True,blank=True)
	title = models.CharField(default='No title', max_length=50)
	photo = models.ImageField('photos/')
	pub_date = models.DateField(auto_now_add=True)
	favorite = models.BooleanField(default=False)
	comment = models.CharField(blank=True, max_length=200)

	def __unicode__(self):
		return self.title

@receiver(post_delete, sender=Photo)
def photo_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.photo.delete(False)
