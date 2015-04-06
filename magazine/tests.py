from django.core import mail
from django.test import TestCase
from django.test.utils import override_settings

@override_settings(EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend')
class EmailTest(TestCase):
    def test_send_email(self):
        # Send message.
        mail_sent_success = mail.send_mail('Subject here', 'Here is the message.',
            '', ['technology@theharvardadvocate.com'],
            fail_silently=False)

        # Test that one message has been sent.
        self.assertEquals(mail_sent_success, 1)