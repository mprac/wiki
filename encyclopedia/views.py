from django.shortcuts import render
from markdown2 import Markdown
from django.http import Http404

from . import util


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
          "title": title
    }
    return render(request, "encyclopedia/entry.html", context)


