from django.shortcuts import render   # Added for this step
from django.http import HttpResponse

# Create your views here.
from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "WebsiteApp/index.html",  
        {
            'title' : "芜湖枚举电子科技有限公司",
            'message' : "欢迎来到芜湖枚举电子科技有限公司",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def about(request):
    return render(
        request,
        "WebSiteApp/about.html",
        {
            'title' : "关于枚举电子信息网",
            'content' : "主编是"+ "程鹏"
        }
    )


def Info_public(request):
    return render(
        request,
        "WebSiteApp/Info_public.html",
        {
        
        }
    )
