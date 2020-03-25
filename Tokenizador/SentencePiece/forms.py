from django.forms import ModelForm
from django import forms
from .models import Tweet

class TweetForm(ModelForm):
	class Meta:
		model = Tweet
		fields = '__all__'
		#fields = ['tweet']
			