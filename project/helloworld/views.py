from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from helloworld.models import Job

def index(request):
   jobs = Job.objects.all()
   context_dict = {'job':jobs}
   return render(request, 'helloworld/index.html', context_dict)
