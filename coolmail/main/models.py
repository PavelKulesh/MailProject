from django.db import models


class Emails(models.Model):
    sender_id = models.IntegerField('Sender')
    recipient_id = models.IntegerField('Recipient')
    topic = models.CharField('Topic', max_length=20)
    text = models.TextField('Text')
    date = models.DateTimeField('Date', auto_now_add=True)
    is_deleted = models.BooleanField('IsDeleted')

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'
        ordering = ['-date']
