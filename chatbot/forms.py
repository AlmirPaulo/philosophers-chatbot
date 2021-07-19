from django import forms

class AskForm(forms.Form):
    question = forms.CharField(label='Type your question here', max_length=100)

