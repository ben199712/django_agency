from django.contrib import admin
from django.http import HttpRequest
from app.models import HeroSection, AboutUs, Counter, Services, Feature, Testimonial, FrequentlyAskQuestions,GeneralInfo, ContactFormLog

# Register your models here.
@admin.register(HeroSection)
class HeroSection(admin.ModelAdmin):
    list_display = [
        'Headline',
    ]

@admin.register(AboutUs)
class AboutUs(admin.ModelAdmin):
    list_display =[
        
        "description",
        "info1",
    ]

@admin.register(Counter)
class Counter(admin.ModelAdmin):
    list_display =[
        "clients",
        "projects",
        "hours_of_support",
        "workers",
    ]

@admin.register(Services)
class Services(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
    ]

@admin.register(Feature)
class Feature(admin.ModelAdmin):
    list_display = [
        "headline",
        "features",
    ]

@admin.register(Testimonial)
class Testimonial(admin.ModelAdmin):
    list_display = [
        "name",
        "position",
    ]

@admin.register(FrequentlyAskQuestions)
class FrequentlyAskQuestions(admin.ModelAdmin):
   pass
  

@admin.register(GeneralInfo)
class GeneralInfo(admin.ModelAdmin):
    list_display = [
        "address",
        "phone_no",
        "email",
    ]

@admin.register(ContactFormLog)
class ContactFormLog(admin.ModelAdmin):
    list_display = [
        "email",
        "is_success",
        "is_error",
        "action_time",

    ]

    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
