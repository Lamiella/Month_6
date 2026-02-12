import os
from datetime import datetime
from time import sleep
from django.core.mail import send_mail
from celery import shared_task
from django.conf import settings


@shared_task
def add(x, y):
    print(f"args: {x}, {y}")
    sleep(25)
    # raise ValueError("TEST ERROR")1
    return x + y

@shared_task
def send_otp(email, code):
    send_mail(
        "Registration",
        f"Confirmation code: {code}",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )

@shared_task
def send_otp_report(email, code):
    send_mail(
        "Report",
        "Something",
        settings.EMAIL_HOST_USER,
        ["alenka110198@gmail.com"],
        fail_silently=False,
    )


@shared_task
def send_welcome_email(email):
    send_mail(
        "Welcome!",
        "Thank you for registration.",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )


@shared_task
def logs_user_login(email):
    with open("logs.txt", "a") as f:
        f.write(f"{email} logged in at {datetime.now()}\n")


@shared_task
def clear_login_logs():
    file_path = "logs.txt"

    if os.path.exists(file_path):
        open(file_path, "w").close()