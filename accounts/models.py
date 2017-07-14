from django.db import models
from django.contrib.auth.models import User





class Profile(models.Model):
	user = models.OneToOneField(User, related_name='profile')
	photo = models.URLField(max_length=500, blank=True, null=True)


	def __str__(self):
		return self.user.username



# Signal for create new profile when a user is added
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
	if kwargs.get('created', False):
		Profile.objects.get_or_create(user=kwargs.get('instance'))