from django import forms
from helloworld.models import JobDB, Priority

class dbForm(forms.ModelForm):
	name = forms.CharField(max_length=20)
	description = forms.CharField(max_length=300)
	date = forms.DateField()
	priority  = forms.CharField(max_length=4)

	class Meta:
		model = JobDB
		fields = ('name', 'description', 'date', 'priority',)
