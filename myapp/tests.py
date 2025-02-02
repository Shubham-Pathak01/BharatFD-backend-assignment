from django.test import TestCase

# Create your tests here.
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
django.setup()

import pytest
from myapp.models import FAQ

@pytest.mark.django_db
def test_faq_creation():
    faq = FAQ.objects.create(question="What is Django?", answer="Django is a Python framework.")
    assert faq.question == "What is Django?"
    assert faq.answer == "Django is a Python framework."

@pytest.mark.django_db
def test_faq_translation():
    faq = FAQ.objects.create(question="Hello", answer="Hi there!")
    translated_hi = faq.get_translated_question("hi")
    assert translated_hi is not None
