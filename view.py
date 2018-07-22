from django.http import HttpReponse
from django.shortcuts import redirect

def index(request):
	return HttpReponse('index')
def login(request):
	return redirect('/index')
