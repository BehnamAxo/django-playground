from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def hello_world(req):
  return HttpResponse("Yo what's up?")

class HelloFromArizona(View):
  def get(self, req):
    return HttpResponse("Yo from Arizona")
