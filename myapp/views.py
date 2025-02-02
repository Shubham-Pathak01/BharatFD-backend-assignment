from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get('lang', 'en')
        faqs = FAQ.objects.all()
        data = []
        for faq in faqs:
            question = faq.get_translated_question(lang)
            data.append({'id': faq.id, 'question': question, 'answer': faq.answer})
        return Response(data)
