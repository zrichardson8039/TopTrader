from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_email(to_email_list, template_subject, template_html, template_text,
               **context):
    """
    Renders templates to context, and uses EmailMultiAlternatives to
    send email.
    """
    if not template_html:
        raise ValueError('No HTML template provided for email.')
    if not template_text:
        raise ValueError('No text template provided for email.')
    if not template_subject:
        raise ValueError('No subject template provided for email.')
    from_email = settings.EMAIL_HOST_USER
    # render the subject, text, and html
    subject = render_to_string(template_subject, context)
    body_text = render_to_string(template_text, context)
    body_html = render_to_string(template_html, context)

    msg = EmailMultiAlternatives(subject, body_text, from_email, to_email_list)
    msg.attach_alternative(body_html, 'text/html')
    msg.send()
