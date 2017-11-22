from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Ruan Andrade', cpf='12345678901',
                    email='ruan.moa@gmail.com', phone='12-98121-3197')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subsctiption_email_to(self):
        expect = ['contato@eventex.com.br', 'ruan.moa@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Ruan Andrade',
            '12345678901',
            'ruan.moa@gmail.com',
            '12-98121-3197'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
