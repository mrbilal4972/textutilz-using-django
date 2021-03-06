# This file is created by me

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello')


def about(request):
    return HttpResponse('<h1>About</h1>')

def read(request):
    f = open('./textutils/first.txt', 'r')
    data = f.read()
    f.close()
    return HttpResponse(data)

def analyze(request):
    params = {
        'name': 'Bilal',
        'place': 'Pakistan'
    }
    return render(request, 'analyze.html', params)

def txtAnalyzer(request):
    # Get text
    djText = request.POST.get('txt', 'noText')
    # Getting CheckBox Selection
    removePunc = request.POST.get('removepunc', 'off')
    removeNewLine = request.POST.get('removeNewLine', 'off')
    spaceRemover = request.POST.get('spaceRemover', 'off')
    upperCase = request.POST.get('upperCase', 'off')
    strLength = request.POST.get('strLength', 'off')
    charCount = request.POST.get('charCount', 'off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ''
    analyzed1 = ''
    analyzed2 = ''
    purpose = ''
    # removePunc Function
    if removePunc == 'on':
        for char in djText:
            if char not in punctuations:
                analyzed += char
        purpose += '- Removed Punctuation '
        djText = analyzed
    # Remove New Line Function
    if removeNewLine == 'on':
        analyzed = ''
        for char in djText:
            if char != '\n' and char != '\r':
                analyzed += char
        purpose += '- Remove New Line '
        djText = analyzed
    # Extra Space Remover Founction
    if spaceRemover == 'on':
        analyzed = ''
        for index, char in enumerate(djText):
            if not(djText[index] == ' ' and djText[index+1] == ' '):
                analyzed += char
        purpose += '- Remove Extra spaces '
        djText = analyzed
    # Converting to Upper Case
    if upperCase == 'on':
        analyzed = djText.upper()
        purpose += '- Convert to Upper Case '
        djText = analyzed
    # Checking String Length
    if strLength == 'on':
        analyzed1 = f"Length of sentence is {len(djText)}"
        purpose += '- String Length '
    # Number of Characters in a String
    if charCount == 'on':
        count = 0
        for char in djText:
            if char != ' ' and char != '\n':
                count += 1
        purpose += '- Number of Characters '
        analyzed2 = f"Number of Characters present are {count}"
    if (removePunc == 'on' or removeNewLine == 'on' or spaceRemover == 'on' or upperCase == 'on' or strLength == 'on' or charCount == 'on') and djText != "":
        params = {'purpose': purpose, 'analyzedTxt': analyzed, 'strLength': analyzed1, 'charCount': analyzed2}
        return render(request, 'analyzedText.html', params)
    else:
        return render(request, 'error.html')

