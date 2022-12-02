from django.db import models
from django.contrib.auth.models import AbstractUser

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
