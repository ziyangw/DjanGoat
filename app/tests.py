# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client

from django.urls import reverse

from models import *

from django.utils import timezone

import views as v


# Create your tests here.
class HttpMethodTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the app index
    # and ensuring the response code is 200 (OK)
    def test_index_route_exists(self):
        response = self.client.get(reverse('app:index'))
        self.assertEqual(response.status_code, 200)

    # Ensure get works
    def test_index_get(self):
        request = self.factory.get('/')
        response = v.index(request)
        self.assertEqual(response.status_code, 200)

    def test_index_post(self):
        request = self.factory.post('/')
        response = v.index(request)
        self.assertEqual(response.status_code, 200)

    def test_index_put(self):
        request = self.factory.put('/')
        response = v.index(request)
        self.assertEqual(response.status_code, 200)

    def test_index_delete(self):
        request = self.factory.delete('/')
        response = v.index(request)
        self.assertEqual(response.status_code, 200)

    def test_index_head(self):
        request = self.factory.head('/')
        response = v.index(request)
        self.assertEqual(response.status_code, 200)

    def test_index_options(self):
        request = self.factory.options('/')
        response = v.index(request)
        self.assertEqual(response.status_code, 200)

    def test_index_trace(self):
        request = self.factory.trace('/')
        response = v.index(request)
        self.assertEqual(response.status_code, 200)


# Models Test
class ModelsTests(TestCase):
    def test_can_create_note(self):
        note = Note(note_name="Hey!", pub_date=timezone.now())

        self.assertEquals(
            str(note),
            'Hey!',
        )