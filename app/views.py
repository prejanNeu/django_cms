from django.shortcuts import render
from .models import Articles

def article_view(request):
    articles=Articles.objects.all().order_by("date")

    return render(request,"article.html",{"articles":articles})
