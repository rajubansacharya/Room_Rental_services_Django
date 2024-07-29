from django.db import models
from django.contrib.auth.models import User

class list_room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images')
    status_choice = [
        ('pending' , 'Pending'),
        ('approved' , 'Approved'),
        ('rejected' , 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=status_choice , default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

