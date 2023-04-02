from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from django.db import models
import markdown2 as mark
import random
from urllib.parse import unquote
import os

from . import util






def wrongmatch(query, files):
    flag = True
    for file in files:
        if query != file:
            flag = False
    return flag


def searchbar(request):
    if request.method == "POST":
        files = util.list_entries()
        # lower case list 
        files = [f.lower() for f in files]
        query = request.POST.get("q").lower()
        util.get_entry(query)
        if query:
            for i in range(len(files)):
                if query == files[i]:
                    with open(f"entries/{query}.md", "r") as f:
                        content = f.read()

                    content = mark.markdown(content)
                    return render(request, "encyclopedia/entry.html",
                                {
                                    "title":query,
                                    "content": content
                                })
           
        
            matches = []
            for file in files:
                if query in file:
                    matches.append(file)
            if matches:
                return render(request, "encyclopedia/search.html",
                            {
                                "file": matches
                            })
          

            return render(request, "encyclopedia/error.html")






def index(request):
    
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def send_data(input):
    return input
def entrys(request, name):
    files = util.list_entries()
    util.get_entry(name)
    name = name.lower()
    
    files = [f.lower() for f in files]   
    flag = True
    for file in files:
        if name == file:
            flag = False

            with open(f"entries/{name}.md", "r") as f:
                content = f.read()

            content = mark.markdown(content)
            break

    if flag == False:
        if name:
            
            global result 
            result = send_data(name)
            edit(request, result)
            return render(request, "encyclopedia/entry.html",
                        {
                            "title": name,
                            "content": content,
                            "result": result
                        })
        
    return render(request, "encyclopedia/error.html")

    
def create(request):
    if request.method == "POST":
        content = request.POST.get("content")
        title = request.POST.get("title")
        if not title.strip() or not content.strip():
                  return render(request, "encyclopedia/newpage.html",
                            {
                            "title":title,
                            "files": util.list_entries()
                            })
        if title in util.list_entries():
            return render(request, "encyclopedia/newpage.html",
                          {
                            "title":title,
                            "files": util.list_entries()
                          })
        else:
             util.save_entry(title, content)
             files = util.list_entries()
             while True:
                for file in files:
                    if title == file:
                        with open(f"entries/{title}.md", "r") as f:
                            content = f.read()

                        content = mark.markdown(content)
                        return render(request, "encyclopedia/entry.html",
                                    {
                                        "title": title,
                                        "content": content,
                                        "result": title
                                    })
                            
            
    return render(request, "encyclopedia/newpage.html")





def edit(request, result):
    global data

    if request.method == "POST":
        # get list of files
        files = util.list_entries()
        

        # deal with case sensitivity
        files = [f.lower() for f in files]


        title = request.POST.get('input-title')        
        prevtitle = request.POST.get('prev-title')   


        # open the file in binary mode and read it
        for i in files:
            with open(f"entries/{prevtitle}.md", "rb") as f:
                content = f.read()
            # write the file in binary to newlines being converted 
            with open(f'entries/{prevtitle}.md', 'wb') as file:
                # convert the user input to binary for writing 
                input_content = request.POST.get('input-content').encode('utf-8')
                content = file.write(input_content)

            # open read file and decode it 
            with open(f"entries/{prevtitle}.md", "rb") as f:
                content = f.read().decode('utf-8')
            content = mark.markdown(content)
            break



        # rename file after each save
        # search for the title in the list
        

        try:    
            util.get_entry(prevtitle)
            i = files.index(prevtitle)
            os.rename(f'entries/{files[i]}.md', f'entries/{title}.md')
            new_title = title
            result = new_title   
        except:
            util.get_entry(prevtitle)
            i = files.index(prevtitle)
            os.rename(f'entries/{files[i]}.md', f'entries/{title}.md')
            new_title = title        
        result = new_title
        

        return render(request, "encyclopedia/entry.html",
                        {
            "content": content,
            "title": new_title,
            "result": result 

                            })
    else:
        

        with open(f"entries/{result}.md", "r") as f:
        
        
            content = f.read()
        
        return render(request, "encyclopedia/edit.html",
        {
            "content": content,
            "result": result,
            "title": result
        })


def random_page(request):
    files = util.list_entries()
    title = random.choice(files)

    with open(f"entries/{(title)}.md", 'r') as file:
        content = file.read()
    content = mark.markdown(content)


    return render(request, "encyclopedia/entry.html",
                  {
                    "title": title,
                    "content": content,
                    "result": title
                  })

    
