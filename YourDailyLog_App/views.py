from django.shortcuts import render

def index(request):
    """The homepage for Your Daily Log"""
    return render(request, "yourdailylog_app/index.html")