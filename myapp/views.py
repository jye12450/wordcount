from django.shortcuts import render

# Create your views here.
# def home(request):
#     return render(request,"home.html")

def home(request):    

    return render(request,"home.html")

def result(request):
    text = request.GET['text']
    list2 = text.split(" ")
    word_count ={}
    for w in list2:
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1
    context={
        "text":text,
        "list2":list2,
        "word_count":word_count,
    }
    return render(request,"result.html",context)

def about(request):
    
    return render(request,"about.html")