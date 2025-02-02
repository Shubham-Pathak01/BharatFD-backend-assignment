from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    question_hi = models.TextField()
    question_bn = models.TextField()

    def get_translated_question(self, language_code):
        translated_field = f'question_{language_code}'
        return getattr(self, translated_field, self.question) or self.question
      

    def save(self, *args, **kwargs):
        translator = Translator()


        if not self.question_hi:
            try:
                self.question_hi = translator.translate(self.question, dest='hi').text
            except Exception as e:
                print(f"Error translating to Hindi: {e}")
                self.question_hi = self.question 

        if not self.question_bn:
            try:
                self.question_bn = translator.translate(self.question, dest='bn').text
            except Exception as e:
                print(f"Error translating to Bengali: {e}")
                self.question_bn = self.question
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question[:50]
