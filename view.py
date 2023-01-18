# I have created this file - chirayu
from django.http import HttpResponse
from django.shortcuts import render

def index(requests):
    return render(requests,'index.html')


def analyze(requests):
    djtext=requests.POST.get('txt','default')

    removepunca = requests.POST.get('removepunc', 'off')

    fullcaps = requests.POST.get('fullcaps', 'off')

    spaceremover = requests.POST.get('spaceremover','off')

    nothing = "nothing to do"

    para = {'purpose':'Error','analyysed text':nothing}

    if removepunca == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyser = ''
        for i in djtext:
            if i not in punctuations:
                analyser = analyser+i
        para = {'purpose': 'Remove punctuations','analyzed_text':analyser}
        djtext = analyser
    if fullcaps == 'on':
        analysed = ""
        for i in djtext:
            analysed = analysed + i.upper()
        para = {'purpose': 'To upper case', 'analyzed_text': analysed}
        djtext = analyser

    if spaceremover == 'on':
        analysed = ""
        for i in djtext:
            if i != " ":
                analysed = analysed + i
        para = {'purpose': 'Space remover', 'analyzed_text': analysed}
        djtext = analyser

    if(removepunca!="on" and fullcaps!='on' and spaceremover != 'on'):
        return HttpResponse('Please select any operation !!')


    return render(requests, 'analyze.html',para)
