import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()

    return render(request, "one/index.html",{
        "one": now.month == 1 and now.day == 1
    })