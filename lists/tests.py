from django.test import TestCase
from django.http import HttpRequest
from lists.views import *
from django.template.loader import render_to_string
from django.core.urlresolvers import resolve


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_returns_correct_html(self):
        request=HttpRequest()
        request.method='POST'
        request.POST['item_text']='A new list item'
        response=home_page(request)
        #self.assertIn('A new list item',response.content.decode())
        expected_html=render_to_string('home.html',{'new_item_text':'A new list item'})
        self.assertEqual(response.content.decode(),expected_html)
