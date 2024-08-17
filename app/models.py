from django.db import models

# Create your models here.
class HeroSection(models.Model):
    Company_name = models.CharField(max_length=255, default='company')
    Headline = models.CharField(max_length=255)
    Paragraph = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.Company_name
    
class AboutUs(models.Model):
    Heading = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    info1 = models.CharField(max_length=250) 
    info2= models.CharField(max_length=250) 
    info3 = models.CharField(max_length=250) 
    info4= models.CharField(max_length=250)

    def __str__(self):
        return self.Heading 
    
class Counter(models.Model):
    clients = models.CharField(max_length=50)
    projects = models.CharField(max_length=50)
    hours_of_support = models.CharField(max_length=50)
    workers = models.CharField(max_length=50)

    def __str__(self):
        return self.clients
    
class Services(models.Model):
    icon = models.CharField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=250, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Feature(models.Model):
    icon = models.CharField(max_length=50, blank=True)
    headline = models.CharField(max_length=250, default="default headline")
    features = models.TextField()

    def __str__(self):
        return self.headline   

class Testimonial(models.Model):
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    quote = models.TextField()

    def __str__(self):
        return self.name
    
class FrequentlyAskQuestions(models.Model):
    question = models.CharField(max_length=250)
    answer = models.TextField()

    def __str__(self):
        return self.question
    
class GeneralInfo(models.Model):
    address = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone_no = models.CharField(max_length=250)
    twitter_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.email
    
class ContactFormLog(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    action_time = models.DateField(null=True, blank=True)
    is_success = models.BooleanField(default=False)
    is_error = models.BooleanField(default=False)
    error_message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email

    