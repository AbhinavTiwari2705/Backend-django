from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python web framework.",
            question_hi="जांगो क्या है?",
            answer_hi="जांगो एक उच्च-स्तरीय पायथन वेब फ्रेमवर्क है।"
        )

    def test_get_translated_text(self):
        self.assertEqual(self.faq.get_translated_text('question', 'en'), "What is Django?")
        self.assertEqual(self.faq.get_translated_text('question', 'hi'), "जांगो क्या है?")

class FAQAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python web framework.",
            question_hi="जांगो क्या है?",
            answer_hi="जांगो एक उच्च-स्तरीय पायथन वेब फ्रेमवर्क है।"
        )

    def test_faq_list(self):
        response = self.client.get(reverse('faq-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_faq_list_hindi(self):
        response = self.client.get(reverse('faq-list') + '?lang=hi')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['question'], "जांगो क्या है?")

