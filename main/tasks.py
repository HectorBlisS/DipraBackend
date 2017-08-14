from celery import task
from .utils import welcome_mail

@task
def mail_welcome(username="BlisS", email="contacto@fixter.org"):
    """
    Task to send  an e-mail notification when user is created.
    """
    return mail_welcome(username, email)
