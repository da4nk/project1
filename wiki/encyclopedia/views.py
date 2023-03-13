from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from django.db import models

from . import util
# use a class

def searchbar(request):
    if request.method == "POST":
        files = util.list_entries()
        query = request.POST.get("q")
        util.get_entry(query)
        if query in files:
            return render(request, f"{query}.md")
        else:
            return HttpResponseRedirect("results")
        
    
    return render(request, "encyclopedia/error.html")



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def entrys(request, name):
    util.get_entry(name)
    try:
        return render(request, f"{name}.md")
    except:
        return render(request, "encyclopedia/error.html")


    
def results(request):
    return render(request, "encyclopedia/search.html")


# class searchbar:

#     def __init__(self, query):
#         self.query = query
    

#     def get_info(self):
#         return self.query 



