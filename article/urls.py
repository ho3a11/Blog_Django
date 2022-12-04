from django.urls import path
from . import views

app_name ='article'
urlpatterns = [
    path('', views.show_article, name='show_article'),
    path('article_detail/<slug>/', views.article_detail, name='article_detail'),
    # path('comment', views.get_comment, name='comment'),
    path('category/<str:category>/', views.article_category, name='category'),
   
]
