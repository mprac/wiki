import random

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from markdown2 import Markdown
from django.http import Http404



from . import util

# Index page
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Entry Page 
def entry(request, title):
    try:
        markdowner = Markdown()
        # get the content using appropriate util function
        getentry = util.get_entry(title)
        # convert markdown to html
        tohtml = markdowner.convert(getentry)
    except TypeError:
        #  error page indicating that their requested page was not found
        return render(request, "encyclopedia/error.html", {'error': 'The requested page was not found'})
    context = {
          "entry": tohtml,
          "title": title,
          "content": getentry
    }
    return render(request, "encyclopedia/entry.html", context)

# Search
def search(request):
    if request.method == "POST":
        query = request.POST['q'].lower()
        entries = util.list_entries()
        lowercase = []
        for x in entries:
            lowercase.append(x.lower())
        if query in lowercase:
            title = request.POST['q']
            for entry in entries:
                if title == entry.lower():
                    return HttpResponseRedirect(reverse('entry', args=(entry,)))
        else:
            options = []
            for entry in entries:
                if query in entry.lower():
                    options.append(entry)
            return render(request, "encyclopedia/searchresults.html", {'options': options })

# new page
def newpage(request):
    return render(request, 'encyclopedia/newpage.html')

# create new page
def createpage(request):
    if request.method == "POST":
        title = request.POST['title'].lower().strip(' .,/')
        content = request.POST['content']
        entries = util.list_entries()
        lowercase = []
        for x in entries:
            lowercase.append(x.lower())
        if title in lowercase:
            return render(request, 'encyclopedia/newpage.html', {'error': 'Page already exists'})
        else:
            title = request.POST['title'].strip(' .,/')
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('entry', args=(title,)))

# edit page
def edit(request, title):
    content = util.get_entry(title)
    context = {
        'title': title,
        'content': content
    }
    return render(request, 'encyclopedia/edit.html', context)

# save post
def saveedit(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse('entry', args=(title,)))

# random page
def randompage(request):
    entries = util.list_entries()
    r = random.choice(entries)
    return HttpResponseRedirect(reverse('entry', args=(r,)))
    


