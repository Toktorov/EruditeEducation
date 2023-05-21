from django.shortcuts import render

from apps.settings.models import Setting, PhoneNumber ,AboutUs

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    about = AboutUs.objects.latest('id')
    return render(request, 'index.html', locals())

def about(request):
    setting = Setting.objects.latest('id')
    about = AboutUs.objects.latest('id')
    return render(request, 'about.html', locals())

def contact(request):
    setting = Setting.objects.latest('id')
    about = AboutUs.objects.latest('id')
    return render(request, 'contact.html', locals())