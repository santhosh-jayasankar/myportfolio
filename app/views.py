from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

def home(request):
    message_sent = False

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
            message_sent = True
        except Exception:
            message_sent = False

    return render(request, "home.html", {
        "message_sent": message_sent
    })
