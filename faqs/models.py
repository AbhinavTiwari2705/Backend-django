from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from .translation import translate_text

class FAQ(models.Model):
    question = models.TextField(_("Question"))
    answer = RichTextField(_("Answer"))
    question_hi = models.TextField(_("Question (Hindi)"), blank=True)
    question_bn = models.TextField(_("Question (Bengali)"), blank=True)
    answer_hi = RichTextField(_("Answer (Hindi)"), blank=True)
    answer_bn = RichTextField(_("Answer (Bengali)"), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = translate_text(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = translate_text(self.question, 'bn')
        if not self.answer_hi:
            self.answer_hi = translate_text(self.answer, 'hi')
        if not self.answer_bn:
            self.answer_bn = translate_text(self.answer, 'bn')
        super().save(*args, **kwargs)

    def get_translated_text(self, field, lang):
        if lang == 'en':
            return getattr(self, field)
        translated_field = f"{field}_{lang}"
        translated_text = getattr(self, translated_field)
        return translated_text if translated_text else getattr(self, field)

    def __str__(self):
        return self.question

