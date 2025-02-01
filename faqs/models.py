from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    # Language-specific fields
    question_hi = models.TextField(null=True, blank=True)
    answer_hi = RichTextField(null=True, blank=True)

    question_bn = models.TextField(null=True, blank=True)
    answer_bn = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.question

    def get_translated_text(self, lang='en'):
        # A method to retrieve the translated question and answer based on the language.
        if lang == 'hi':
            return self.question_hi or self.question, self.answer_hi or self.answer
        elif lang == 'bn':
            return self.question_bn or self.question, self.answer_bn or self.answer
        else:
            return self.question, self.answer
