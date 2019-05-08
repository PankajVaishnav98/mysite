from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_protect
#from django.utils.decorators import method_decorator

#method_decorator(csrf_protect)
def index(request):
    return render(request, 'index.html')
def contact(request):
    print("hello form submitted")
    return  render(request, 'index.html')