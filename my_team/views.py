from django.shortcuts import render

def hi(request):
    return render(request, "hi.html")

def hello(request):
    sentence = request.GET['sentence']

    wordList = sentence.split(',')

    
    return render(request, "hello.html",{'sentence':sentence, 'count':len(wordList),'wordList': wordList})

