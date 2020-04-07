from django.contrib import admin

from .models import TextTestimonial, Tag, WritingPrompt

admin.site.register(TextTestimonial)
admin.site.register(WritingPrompt)
admin.site.register(Tag)
