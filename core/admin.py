from django.contrib import admin

from .models import Question, Answer

admin.site.site_header = 'DevelopersAsk Administration'

admin.site.register(Question)
admin.site.register(Answer)