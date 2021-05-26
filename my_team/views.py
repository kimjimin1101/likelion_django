from django.shortcuts import render

def hi(request):
    return render(request, "hi.html")

def hello(request):
    sentence = request.GET['sentence']

    wordList = sentence.split(',')


    return render(request, "hello.html",{'sentence':sentence, 'count':len(wordList),'sentence1': sentence.split(',')[0],'sentence2':sentence.split(',')[1],'sentence3':sentence.split(',')[2],'sentence4':sentence.split(',')[3]})

