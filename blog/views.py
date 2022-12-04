from django.shortcuts import render,redirect
from article.models import Category, Article,voite_user
from django.views.generic import ListView
import datetime


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
    


    
def category_list(request):
    category_list = Category.objects.all()
    context = {
        "category_list": category_list,
    }

    return context

def about(request):
    context = {
        'name':'name'
    }
    return render(request,'about.html',context=context)


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
    
    

