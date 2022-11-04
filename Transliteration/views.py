from django.shortcuts import render
from .models import Transliteration
import requests
import json
from django.http import HttpResponse,JsonResponse
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def Trans(request):
    # Trans = Transliteration.objects.all()
    lang = [
        {'id':'tamil',
        'name':'Tamil'},
        {'id':'hindi',
        'name':'Hindi'},
        {'id':'telugu',
        'name':'Telugu'},
        {'id':'bengali',
        'name':'Bengali'},
        {'id':'gujarati',
        'name':'Gujarati'},
        {'id':'marathi',
        'name':'Marathi'},
        {'id':'kannada',
        'name':'Kannada'},
        {'id':'malayalam',
        'name':'Malayalam'},
        {'id':'punjabi',
        'name':'Punjabi'},
        {'id':'nepali',
        'name':'Nepali'},
    ]
    C = {
        # 'Transliteration': Trans,
        'language':lang,
        # 'stats':ur
    }
    C.update(csrf(request))
    return render(request, 'Transliteration.html', C)
    
@csrf_exempt
def predict(request):

    print('vidya')

    data = request.GET.get('data')
    lang = request.GET.get('lang')
    print('vidyaaaa')
    print(data,lang)
    url = 'http://xlit.quillpad.in/quillpad_backend2/processWordJSON?lang=' + lang + '&inString=' + data
    print(url)
    # r = requests.get('http://xlit.quillpad.in/quillpad_backend2/processWordJSON?lang=tamil&inString=namaste')
    r = requests.get(url)
    print(r.status_code)

    if r.status_code == 200:
        options =r.json()['twords'][0]['options']

    message = "success"
    return JsonResponse({ 'message': message,
                    'options':options,})

