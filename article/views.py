from django.shortcuts import render,redirect
from . models import Article,Category,Comment,voite_user
from . import forms
from django.contrib.auth.decorators import login_required
import socket
from django.core.paginator import Paginator

def show_article(request):
    res = Article.objects.all()
    
    return render(request,'show_article.html', {'articles':res})


def article_category(request,category):
    
    # system = socket.gethostname()
    # IPAddr = socket.gethostbyname(system)
    # print(f'user ip is :{IPAddr}')
    articlecat =  Article.objects.filter(category__title =category).order_by('-date')
    paginator = Paginator(articlecat, 2) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for p in page_obj:
      print(f"saddsfsdfdsfsdf534545cdxvsads --->>> {p.date.day}")
      

    context = {
        'cat': category,
        'page':page_obj
        
    }
    return render(request,'category.html', context=context)


def show_comment(arg):
    return Comment.objects.filter(article=arg)

def save_voite(request,detail):
    try:
        user =voite_user.objects.get(article=detail) 
   
        if request.method=='POST':
            form = forms.VoiteForm(request.POST,instance=user)
            if form.is_valid():
                form.save()
        form = forms.VoiteForm(instance=user)
        return form
    except:
        if request.method=='POST':
            form = forms.VoiteForm(request.POST)
            if form.is_valid():
                    exp = form.save(commit=False)
                    exp.article = detail
                    exp.user =request.user
                    exp.save()
        form = forms.VoiteForm()
        return form

        
    
@login_required
def get_comment(request,detail):
    if request.method=='POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
           exp = form.save(commit=False)
           exp.article = detail
           exp.user =request.user
           exp.save()
    form = forms.CommentForm()

    return form

def article_detail(request, slug):

    detail = Article.objects.get(slug= slug)
    # comments = Comment.objects.filter(article=detail)
    recent = Article.objects.all().order_by('-date')[:3]
    comments = show_comment(detail)
    count_com = len(comments)
    voite = save_voite(request,detail)
    if request.user:
        form = get_comment(request,detail)
    context ={
        'detail':detail,
        'form': form ,
        'comments': comments,
        'voite' : voite,
        'count_com': count_com,
        'recent':recent
    }
    if request.method!='POST':
            detail.visit+=1
            Article.save(detail)
    return render(request, 'article_detail.html', context=context)




    
            
        
