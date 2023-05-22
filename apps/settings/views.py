from django.shortcuts import render

from apps.settings.models import Setting, PhoneNumber, AboutUs, Teacher, Benefits, Gallery, Review

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    about = AboutUs.objects.latest('id')
    phones = PhoneNumber.objects.filter(setting=setting.id)
    benefits = Benefits.objects.all().order_by('?')
    index_benefits_one = Benefits.objects.all()[:3]
    index_benefits_two = Benefits.objects.all()[3:]
    gallery = Gallery.objects.all().order_by('?')
    reviews = Review.objects.all().order_by('?')
    return render(request, 'index.html', locals())

def about(request):
    setting = Setting.objects.latest('id')
    about = AboutUs.objects.latest('id')
    teachers = Teacher.objects.all()
    index_benefits_one = Benefits.objects.all()[:3]
    index_benefits_two = Benefits.objects.all()[3:]
    return render(request, 'about.html', locals())

def contact(request):
    setting = Setting.objects.latest('id')
    about = AboutUs.objects.latest('id')
    phones = PhoneNumber.objects.filter(setting=setting.id)
    return render(request, 'contact.html', locals())

def client_form(request):
    setting = Setting.objects.latest('id')
    return render(request, 'client_form.html', locals())

def benefits(request):
    setting = Setting.objects.latest('id')
    benefits = Benefits.objects.all().order_by('?')
    reviews = Review.objects.all().order_by('?')
    return render(request, 'benefits.html', locals())