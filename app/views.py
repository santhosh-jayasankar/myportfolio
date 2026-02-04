from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        try:
            send_mail(
                subject="New Contact Message - Portfolio",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            messages.success(request, "Message sent successfully!")
        except Exception:
            messages.error(request, "Message failed. Please try again later.")

    return render(request, "home.html")
