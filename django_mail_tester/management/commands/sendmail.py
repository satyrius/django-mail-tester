import datetime
from optparse import make_option

from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option(
            '-e', '--email', '--email-to', action='store', dest='email',
            help='Email to send to'),
        make_option(
            '-f', '--from', '--email-from', action='store', dest='from',
            help='Email to send from. It is SERVER_EMAIL by default'),
        make_option(
            '-s', '--subject', action='store', dest='subject',
            default='Test email by sendmail command', help='Email subject'),
    )

    def handle(self, *args, **options):
        message = u' '.join(args)
        if not message:
            message = 'Test email sending'
        message += u'\nGenerated at {now}'.format(now=datetime.datetime.now())

        email_to = options['email']
        assert email_to
        email_from = options['from'] or settings.SERVER_EMAIL
        send_mail(options['subject'], message, email_from, [email_to])
