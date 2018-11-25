from django.shortcuts import render   # Added for this step
from django.http import HttpResponse

# Create your views here.
from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "WebsiteApp/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title' : "Website",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def about(request):
    return render(
        request,
        "WebSiteApp/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )
