from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

from . import util
# use a class
def searchbar(request, name):
    
    if request.method == "POST":
        query = request.POST.get("q")
        util.get_entry(name)
        possible_querys = {
            "name": name
        }
        for i in possible_querys:
            if query in possible_querys[i]:
                return render(request, f"{query}.md")
            else:
                return HttpResponseRedirect("results")
    else: 
        query = ""
    return query

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "query": entry
    })
    
def entrys(request, name):
    util.get_entry(name)
    try:
        return render(request, f"{name}.md")
    except:
        return render(request, "encyclopedia/error.html")


    
def results(request):
    return render(request, "encyclopedia/error.html")
