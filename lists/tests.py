from django.test import TestCase
from django.http import HttpRequest
from lists.views import *
from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from lists.models import Item


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_can_save_a_POST_request(self):
        request=HttpRequest()
        request.method='POST'
        request.POST['item_text']='A new list item'
        response=home_page(request)
        self.assertEqual(Item.objects.count(),1)
        new_item=Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')

        self.assertIn('A new list item',response.content.decode())
        expected_html=render_to_string('home.html',{'new_item_text':'A new list item'})
        self.assertEqual(response.content.decode(),expected_html)

    def test_home_page_returns_correct_html(self):
        request=HttpRequest()
        request.method='POST'
        request.POST['item_text']='A new list item'
        response=home_page(request)
        #self.assertIn('A new list item',response.content.decode())
        expected_html=render_to_string('home.html',{'new_item_text':'A new list item'})
        self.assertEqual(response.content.decode(),expected_html)

    def test_home_page_only_saves_items_when_necessary(self):
        request=HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(),0)

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item=Item()
        first_item.text='The first (ever) list item'
        first_item.save()

        second_item=Item()
        second_item.text='Item the second'
        second_item.save()

        saved_items=Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item=saved_items[0]
        second_saved_item=saved_items[1]
        self.assertEqual(first_saved_item.text,'The first (ever) list item')
        self.assertEqual(second_saved_item,'Item the second')


