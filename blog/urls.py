from django.urls import path
from . import views

# Defines the application namespace for this set of URLs.
app_name='blog'
# Defines URL patterns for the blog application.
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
     path('contact/', views.contact, name='contact'),
    # path('categories/', views.category_list, name='category_list'),
    # path('category/<category>/', views.CatListView.as_view(), name='category'),

]