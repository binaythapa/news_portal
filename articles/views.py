from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

#article
def article(request):
    if request.method== "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form= ArticleForm()
    return render(request, 'articles/create.html', {'form':form})

def edit_article(request, id):
    article = get_object_or_404(Article, pk=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', id=article.id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/create.html', {'form': form})

'''
def article_detail(request, id):
    articles = Article.objects.all()
    article = get_object_or_404(Article, pk=id)
    category= Category.objects.all() 
    view, created = View.objects.get_or_create(article=article)
    view.count += 1   
    view.save()
    return render(request, "articles/common.html", {'article': article, 'view_count': view.count,"categories":category,"articles":articles})
'''

from django.shortcuts import render, get_object_or_404
from .models import Article, Category, View

def article_detail(request, id):
    # Retrieve the requested article
    article = get_object_or_404(Article, pk=id)
    
    # Increment view count
    view, created = View.objects.get_or_create(article=article)
    view.count += 1   
    view.save()
    
    # Retrieve all articles
    articles = Article.objects.all()
    
    # Retrieve all categories
    categories = Category.objects.all()
    
    # Filter related news based on category of the current article
    related_news = Article.objects.filter(category=article.category).exclude(id=article.id)[:3]
    
    # Render the article detail page with relevant data
    return render(request, "articles/article_detail.html", {
        'article': article,
        'view_count': view.count,
        'categories': categories,
        'articles': articles,
        'related_news': related_news  # Pass related news to the template
    })


def article_delete(request, id):    
    data = get_object_or_404(Article, pk=id)
    data.delete()
    return redirect("/")

#category
def category(request):
    if request.method== "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form= CategoryForm()
    return render(request, 'articles/create.html', {'form':form})

def category_detail(request,id):
    data = get_object_or_404(Category, pk=id)
    return render(request, "articles/article_detail.html", {'data':data})

def category_delete(request, id):    
    data = get_object_or_404(Category, pk=id)
    data.delete()
    return redirect("/")

#Tag
def tag(request):
    if request.method== "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form= TagForm()
    return render(request, 'articles/create.html', {'form':form})

def tag_detail(request,id):
    data = get_object_or_404(Tag, pk=id)
    return render(request, "articles/article_detail.html", {'data':data})

def tag_delete(request, id):    
    data = get_object_or_404(Tag, pk=id)
    data.delete()
    return redirect("/")




