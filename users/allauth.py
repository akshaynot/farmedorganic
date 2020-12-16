from django.shortcuts import render
from django.urls import reverse
from allauth.account.adapter import DefaultAccountAdapter


#Custom allauth adapter:
class AccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        return reverse('profile')

    def get_next_redirect_url(self , request):
        return reverse('profile')
    

