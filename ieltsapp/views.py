from django.shortcuts import render
#from django.http import HttpResponse
from .models import Articles

def index(request):
    latest_articles_list = Articles.objects.order_by('-pub_date')[:5]
    context = {'latest_articles_list': latest_articles_list}
    return render(request, 'ieltsapp/index.html', context)
