from django.shortcuts import render, redirect
from django.core.mail import send_mail
from app.models import (HeroSection, AboutUs, Counter, Services, Feature, 
                        Testimonial, FrequentlyAskQuestions, GeneralInfo, ContactFormLog)
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils import timezone

# Create your views here.
def index(request):

    all_records = HeroSection.objects.first()

    aboutus = AboutUs.objects.first()

    counter = Counter.objects.first()

    services = Services.objects.all()

    feature = Feature.objects.all()

    testimonial = Testimonial.objects.all()

    faqs = FrequentlyAskQuestions.objects.all()

    general = GeneralInfo.objects.first()

    context = {
        "company_name": all_records.Company_name,
        "headline": all_records.Headline,
        "paragraph": all_records.Paragraph,
        "image": all_records.image,

        "aboutus": aboutus,

        "services": services,

        "counter": counter,

        "feature": feature,

        "testimonial": testimonial,

        "faqs": faqs,

        "general": general,
    }

    return render(request, "index.html", context)



def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        #email templates format
        context = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message,
        }
        html_content = render_to_string('emails.html', context)

        #error message variables
        is_error = False
        is_success = False
        error_message =""

        #sending mall()
        try:
            send_mail(
                subject = subject,
                message =None,
                html_message= html_content,
                from_email = settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
        except Exception as e:
            is_error = True
            error_message = str(e)
            messages.error(request, "the message failed to send")
        else:
            is_success =True
            messages.success(request, "message was sent successfully")

            #contact form logs 
            ContactFormLog.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
                action_time=timezone.now(),
                is_success=is_success,
                is_error=is_error,
                error_message=error_message,
            )
    return redirect('home')
