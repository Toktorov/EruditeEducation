from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Описание"
    )
    logo = models.ImageField(
        upload_to='logo/'
    )
    email = models.EmailField(
        verbose_name="Почта",
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name="Ссылка на Instagram",
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name="Ссылка на Facebook",
        blank=True, null=True
    )
    whatsapp = models.URLField(
        verbose_name="Ссылка на Whats App",
        blank=True, null=True
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес школы",
        blank=True, null=True
    )
    url_address = models.URLField(
        verbose_name="Ссылка на адрес",
        blank=True, null=True
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

class PhoneNumber(models.Model):
    setting = models.ForeignKey(
        Setting, on_delete=models.CASCADE,
        related_name="setting_phone",
        verbose_name="Настройка"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )

    def __str__(self):
        return f"{self.setting} {self.phone}"
    
    class Meta:
        verbose_name = "Телефонный номер"
        verbose_name_plural = "Телефонные номера"

class AboutUs(models.Model):
    description = models.TextField(
        verbose_name="Описание"
    )

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

class Benefits(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.CharField(
        max_length=300,
        verbose_name="Описание"
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"

class Teacher(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    subject = models.CharField(
        max_length=255,
        verbose_name="Предмет"
    )
    image = models.ImageField(
        upload_to='teams/',
        verbose_name="Фотография",
        blank=True, null=True
    )

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"

class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"