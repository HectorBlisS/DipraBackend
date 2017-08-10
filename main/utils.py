from django.template.loader import get_template
from django.core.mail import EmailMessage

empty_request = {
	"to":"",
	"from_email":"hola@planb.com.mx",
	"user":None,
	"message":None,
	"subject":"Dipra",
	"template":"mail/default.html",
	"ctx":{}

}

def enviar_mails(data=empty_request):
	# message=get_template("patrocinioMail.html").render(Context(ctx))
	# message=get_template(template).render()
	message=get_template(data["template"]).render(data["ctx"])
	msg=EmailMessage(data["subject"],message, bcc=data["to"],from_email=data["from_email"])
	msg.content_subtype='html'
	msg.send()