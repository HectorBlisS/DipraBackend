from django.template.loader import get_template
from django.core.mail import EmailMessage

data = {
    "to": ["contacto@fixter.org", ],
    "from_email": "hola@planb.com.mx",
    "subject": "Dipra Notifyer",
    "template": "mail/default.html",
    "ctx": {
        "titulo": "¡Te damos la Bienvenida!",
        "subtitulo": "Estmos muy contentos de que te hayas unido a nuestra comunidad",
        "parrafo1": "SY estamos invitación a las Sedes interesadas, si gustan acompañarnos, sería un gusto poderles conocer y conozcan más sobre nuestra labor educativa que realizamos a través de las Sedes de Educación Regional en los diferentes estados.",
        "parrafo2": "Cada año tenemos una reunión anual de directivos de Sedes de Bachillerato, que hemos llamado nuestra convención educativa 2017, donde bien de diferentes estados donde hay una Sede de Educación Regional que son tiempos de koinonía, revisión de situaciones en cada Sede, temas a discutir sobre la educación y educación cristiana, proyectos y apretura de Sedes, entre otros temas.",
        "username": "bliss",
    }
}


def enviar_mails(data=data):
    data['ctx']["username"] = "crusemo"
    # message=get_template("patrocinioMail.html").render(Context(ctx))
    # message=get_template(template).render()
    message = get_template(data["template"]).render(data["ctx"])
    msg = EmailMessage(data["subject"], message, bcc=data["to"], from_email=data["from_email"])
    msg.content_subtype = 'html'
    msg.send()


def welcome_mail(username="BlisS", email="contacto@fixter.org"):
    data["ctx"]["username"] = username
    data["to"] = [email]
    # message=get_template("patrocinioMail.html").render(Context(ctx))
    # message=get_template(template).render()
    message = get_template(data["template"]).render(data["ctx"])
    msg = EmailMessage(data["subject"], message, bcc=data["to"], from_email=data["from_email"])
    msg.content_subtype = 'html'
    return msg.send()
