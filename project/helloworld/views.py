from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest
from helloworld.models import JobDB
from helloworld.forms import dbForm

def index(request):
   jobs = Job.objects.all()
   context_dict = {'job':jobs}
   return render(request, 'helloworld/index.html', context_dict)

def angular(request):
   return render(request, 'helloworld/angular.html')

def database(request):

   if request.method == 'POST':
	form = dbForm(request.POST)
	if form.is_valid():
		name = form.cleaned_data['name']
		description = form.cleaned_data['description']
		date = form.cleaned_data['date']
		priority = form.cleaned_data['priority']
		post = JobDB(name=name,	description=description, date=date, priority=priority)
		
		post.save()
		return HttpRequestRedirect(reverse('database'))
	else: 
		form.errors
   else:
	form = dbForm()

   return render(request, 'helloworld/database.html', { 'form': dbForm, })

