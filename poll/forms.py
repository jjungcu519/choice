from django import forms
from .models import Poll,Comment

class PollForm(forms.ModelForm):
    class Meta():
        model = Poll
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        exclude = ('poll',)