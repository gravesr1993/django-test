from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from restaurants.models import RestaurantLocation

class Item(models.Model):
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL)
	restaurant		= models.ForeignKey(RestaurantLocation)
	name 			= models.CharField(max_length=120)
	content 		= models.TextField(help_text='seperate each item by comma')
	excludes		= models.TextField(blank=True,null=True, help_text='seperate each item by comma')
	public 			= models.BooleanField(default=True)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)
	# image_url

	class Meta:
		ordering = ['-updated','-timestamp'] #reverse item.object.all to give recent updated item first
	def get_content(self):
		return self.content.split(",")
	def get_excludes(self):
		return self.excludes.split(",")
	def get_absolute_url(self):#get_absolute_url
		return reverse('menus:detail',kwargs={'pk':self.pk})
	def __str__(self):
		return self.name