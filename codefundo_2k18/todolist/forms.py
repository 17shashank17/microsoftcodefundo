from django.db import models
from django import forms
from todolist.models import liste
from .models import liste

class input(forms.Form):
	list_todo=forms.CharField(max_length=200)
	def save(self):
		new_entry=liste.objects.create(
		list_todo=self.cleaned_data['list_todo'],
		)
		return new_entry
	
