import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FAQ_Model.settings")
django.setup()


import pytest
from rest_framework.test import APIClient
from myapp.models import FAQ

@pytest.mark.django_db
def test_faq_api():
    client = APIClient()
    FAQ.objects.create(question="What is Python?", answer="Python is a programming language.")
    response = client.get('/api/faqs/?lang=en')
    # print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0
 