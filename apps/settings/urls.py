from django.urls import path

from apps.settings.views import index, about, contact, client_form, benefits


urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('form/', client_form, name="client_form"),
    path('benefits/', benefits, name="benefits"),
]