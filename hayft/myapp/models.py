from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.timezone import now as utcnow

class CustomUser(AbstractUser):
    extra_kwargs = {'password': {'write_only': True}}
    def __str__(self):
        return self.username
    

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    emoji = models.CharField(max_length=10)
    text_content = models.CharField(max_length=500000)
    created_at = models.DateTimeField(auto_now_add=True)
