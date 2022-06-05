from django.db import models
from django.contrib.auth.models import User


class Email(models.Model):
    """This class describes the model in the database"""
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='sender')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='recipient')
    topic = models.CharField(max_length=20)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.topic

    class Meta:
        indexes = [models.Index(fields=['sender', 'recipient', 'topic', 'text', 'date'])]
        ordering = ['-date']
