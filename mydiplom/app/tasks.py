from celery.decorators import task
import logging
from django.conf import settings
from django_rest_passwordreset.signals import reset_password_token_created
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from mydiplom.celery import app
from app.models import ConfirmEmailToken, User
from django.core.mail import EmailMultiAlternatives

@app.task
def password_reset_token_created(sender, instance, reset_password_token, **kwargs):
    """
    Отправляем письмо с токеном для сброса пароля
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param kwargs:
    :return:
    """
    # send an e-mail to the user

    send_mail(
        # title:
        f"Password Reset Token for {reset_password_token.user}",
        # message:
        reset_password_token.key,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email],
        fail_silently=False,
    )


@app.task
def new_user_registered_signal(user_id, **kwargs):
    # send an e-mail to the user

    token, _ = ConfirmEmailToken.objects.get_or_create(user_id=user_id)

    send_mail(
        # title:
        f"Password Reset Token for {token.user.email}",
        # message:
        f'{token.key}',
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [token.user.email],
        fail_silently=False,
    )

@app.task
def new_order(user_id, **kwargs):
    """
    отправяем письмо при изменении статуса заказа
    """
    # send an e-mail to the user
    user = User.objects.get(id=user_id)

    send_mail(
        # title:
        f"Обновление статуса заказа",
        # message:
        'Заказ сформирован',
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [user.email],
        fail_silently=False,
    )