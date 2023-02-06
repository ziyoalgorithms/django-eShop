from django.core.mail import send_mail, get_connection


conn = get_connection(backend='django.core.mail.backends.smtp.EmailBackend')


def send_mail_to_user(subject, message, *user_email):
    send_mail(
        subject,
        message,
        'studiovisual0077@gmail.com',
        user_email,
        fail_silently=False,
        connection=conn,
    )
