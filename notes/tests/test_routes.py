from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from notes.models import Note

class TestRoutes(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.notes = Note.objects.create(title='Заголовок', text='Текст')
    
    def test_pages_availibility(self):
        urls = (
            ('',),
            ('',),
            ('',),
            ('',),
            ('',),
            ('',),
        )
        for name, args in urls:
            with self.subTest(name=name):
                url = reverse(name, args=args)
                response = self.client.get(url)
                self.assertEqual(response.status_code, HTTPStatus.OK)
        
