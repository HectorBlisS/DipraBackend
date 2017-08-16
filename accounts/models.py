from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# from main.utils import welcome_mail
from main.tasks import bienvenida



class Profile(models.Model):

	TIPOS=(
		('general','general'),
		('cliente','cliente'),
		('asesor','asesor'),
		('reclutador','reclutador'),
		('both','both')
	)
	user = models.OneToOneField(User, related_name='profile')
	photo = models.URLField(max_length=500, blank=True, null=True)
	tipo = models.CharField(max_length=100, choices=TIPOS, default="cliente" )
	asesorId = models.CharField(max_length=100, blank=True, null=True)
	clienteId = models.CharField(max_length=100, blank=True, null=True)
	aprobado = models.BooleanField(default=False)
	def __str__(self):
		return self.user.username


# SIGNALS


# Signal for create new profile when a user is added
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=kwargs.get('instance'))


# Signal for create token for each user
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        print('llamando task')
        bienvenida.delay(username=instance.username, email=instance.email)
    # try:
    #     print("Enviando bienvenida")
    #     welcome_mail(username=instance.username, email=instance.email)
    # except:
    #     print("error mail")

