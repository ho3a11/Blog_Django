from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
     path('contact/', views.contact, name='contact'),
    # path('categories/', views.category_list, name='category_list'),
    # path('category/<category>/', views.CatListView.as_view(), name='category'),

]