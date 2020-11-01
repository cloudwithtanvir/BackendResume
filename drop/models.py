from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# import PyPDF2
from ckeditor.fields import RichTextField
from pdfminer.high_level import extract_text

from rest_framework.decorators import api_view
# Create your models here.

class Drop(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=11)
    tech_expert =models.JSONField()
    # language_expert = models.CharField(max_length=100)
    upload = models.FileField(upload_to='uploads/')
    cv_text = RichTextField(null=True, blank=True)
    comments = models.CharField(max_length=500)
    position = models.CharField(max_length=150)
    heard = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return '{0}'.format(self.name)



@receiver(post_save, sender=Drop)
def post_save_pdf(sender, instance, created, *args, **kwargs):
    if created:
        #pdfobj = open(instance.upload.path, "rb")
        #pdfread = PyPDF2.PdfFileReader(pdfobj)
        text = extract_text(instance.upload.path)

        #for i in range(pdfread.numPages):
        #    pob = pdfread.getPage(i)
        #    text += pob.extractText()
        instance.cv_text = text
        instance.save()
