from django.http import HttpResponse
from django.shortcuts import render
import joblib

def index (request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def ourteams(request):
    return render(request, "ourteams.html") 

def ourservices(request):
    return render(request, "ourservices.html")
    
def result(request):

    CL = joblib.load("FinalModel.sav")

    lst = []

    lst.append(float(request.GET["N"]))
    lst.append(float(request.GET["P"]))
    lst.append(float(request.GET["K"]))
    lst.append(float(request.GET["temperature"]))
    lst.append(float(request.GET["ph"]))
    lst.append(float(request.GET["rainfall"]))

    print(lst)

    ans = CL.predict([lst])

    A = ans.tolist()
    ANS = ' '.join(map(str, A))
    print(ANS)

    return render(request, "result.html", {"ans": ANS, "lst": lst})