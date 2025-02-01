from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        # Create a sample FAQ with translations
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework.",
            question_hi="डjango क्या है?",
            answer_hi="डjango एक वेब फ्रेमवर्क है।",
            question_bn="ডjango কি?",
            answer_bn="ডjango একটি ওয়েব ফ্রেমওয়ার্ক।"
        )

    def test_faq_creation(self):
        # Test that the FAQ is created correctly
        self.assertEqual(self.faq.question, "What is Django?")
        self.assertEqual(self.faq.answer, "Django is a web framework.")

    def test_multilingual_support(self):
        # Test multilingual content
        self.assertEqual(self.faq.question_hi, "डjango क्या है?")
        self.assertEqual(self.faq.answer_hi, "डjango एक वेब फ्रेमवर्क है।")
        self.assertEqual(self.faq.question_bn, "ডjango কি?")
        self.assertEqual(self.faq.answer_bn, "ডjango একটি ওয়েব ফ্রেমওয়ার্ক।")
