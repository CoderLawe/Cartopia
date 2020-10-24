    
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from .import forms
from bs4 import BeautifulSoup
import requests

#source = requests.get("https://www.caranddriver.com/reviews/").text

def article_list(request):
    articles = Article.objects.all().order_by('date');
    return render(request, 'articles/article_list.html', { 'articles': articles,})

def article_detail(request, slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', { 'article': article })

def article_create(request):
	if request.method == 'POST':
		form = forms.CreateArticle(request.POST)
		if form.is_valid():
			instance = form.save(commit = False)
			#instance.author = request.user
			instance.save()
			return redirect('list')

	else:
		form = forms.CreateArticle()
	return render(request, 'articles/article_create.html',{'form':form})
