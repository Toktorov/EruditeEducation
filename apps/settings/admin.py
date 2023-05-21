from django.contrib import admin

from apps.settings.models import Setting, PhoneNumber, AboutUs, Benefits, Contact, Teacher, Gallery, Review

# Register your models here.
@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'logo')

@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('setting', 'phone')

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('description', )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name', 'phone')
    list_per_page = 20

@admin.register(Benefits)
class BenefitsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    search_fields = ('name', 'subject')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image', )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'text')
    search_fields = ('name', 'position', 'text')
    list_per_page = 20