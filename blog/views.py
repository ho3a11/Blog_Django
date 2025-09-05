from django.shortcuts import render,redirect
from article.models import Category, Article,voite_user
from django.views.generic import ListView
import datetime


# Renders the homepage with recent articles, most visited articles, and top-voted articles.
def index(request):
    articles = Article.objects.all().order_by("-date")[:3]
    
    visit = Article.objects.all().order_by("-visit")[:5]
    
    voite = voite_user.objects.all().order_by("-voite")[:5]
    context = {
        'articles':articles,
        'voite':voite,
        'visit':visit,
       
    }
    
    return render(request, 'index.html',context=context)
    


    
# Retrieves a list of all categories.
def category_list(request):
    category_list = Category.objects.all()
    context = {
        "category_list": category_list,
    }

    return context

# Renders the about page.
def about(request):
    context = {
        'name':'name'
    }
    return render(request,'about.html',context=context)

# Renders the contact page.
def contact(request):
    context = {
        'name':'name'
    }
    return render(request,'contact.html',context=context)


# def most_voite(request):
#     voite = voite_user.objects.all().order_by("-voite")[:5]
#     context = {
#         'voite':voite
#     }
    
#     return render(request, 'index.html',context=context)
    



# def category_list(request):
#     cat_list = Category.objects.all()
#     # cat = Category.objects.get(pk=id)
#     context = {
#         'category_list' :cat_list
#         # 'category': cat
#     }
    
#     return context


# class CatListView(ListView):
#     template_name = 'category.html'
#     context_object_name = 'catlist'

#     def get_queryset(self):
#         content = {
#             'cat': self.kwargs['category'],
#             'posts': Article.objects.filter(category__title=self.kwargs['category'])
#         }
#         return content
    
    

