from django.shortcuts import render

from apps.settings.models import Setting, PhoneNumber, AboutUs, Teacher

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    about = AboutUs.objects.latest('id')
    phones = PhoneNumber.objects.filter(setting=setting.id)
    return render(request, 'index.html', locals())

def about(request):
    setting = Setting.objects.latest('id')
    about = AboutUs.objects.latest('id')
    teachers = Teacher.objects.all()
    return render(request, 'about.html', locals())

def contact(request):
    setting = Setting.objects.latest('id')
    about = AboutUs.objects.latest('id')
    phones = PhoneNumber.objects.filter(setting=setting.id)
    return render(request, 'contact.html', locals())

def client_form(request):
    setting = Setting.objects.latest('id')
    return render(request, 'client_form.html', locals())