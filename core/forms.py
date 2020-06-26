from django import forms

from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body']
        labels = {
            'title': 'Question',
            'body': 'Details',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Enter your question title here.'