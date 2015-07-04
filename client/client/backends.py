from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.conf import settings

import requests

__all__ = ['SSOBackend']

User = get_user_model()

class SSOBackend(ModelBackend):

    def authenticate(self, username, password):

        response = requests.get(settings.SSO_SERVER,
            headers={
                'X-Auth-Username': username,
                'X-Auth-Password': password
            })
        
        if response.status_code != requests.codes.ok:
            return None

        user_data = response.json()

        user, created = User.objects.get_or_create(username=username,
            defaults={
                'email': user_data['email'],
                'is_staff': True,
                'is_superuser': True
            })
        if user.email != user_data['email']:
            user.email = user_data['email']
            user.save()

        return user

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None