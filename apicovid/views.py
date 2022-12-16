

# Create your views here.
from django.shortcuts import render
import requests

CEP='22280020'

def home(request):
    response = requests.get('https://viacep.com.br/ws/'+ CEP+'/json/').json()
   
    return render(request, 'home.htm', {'response': response})