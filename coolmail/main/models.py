from django.db import models


class Email(models.Model):
    sender = models.CharField('Sender', max_length=20)
    recipient = models.CharField('Recipient', max_length=20)
    topic = models.CharField('Topic', max_length=200)
    text = models.TextField('Text')
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.topic
