from celery import task
from django.core.mail import send_mail
from .models import Email


@task
def email_created(email_id):
    email = Email.objects.get(id=email_id)
    subject = 'Order nr. {}'.format(email_id)
    message = 'Dear {},\n\nYou have successfully sent an email.\
                Your email id is {}.'.format(email.sender,
                                             email.id)
    mail_sent = send_mail(subject,
                          message,
                          [email.email])
    return mail_sent
