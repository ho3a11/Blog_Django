from . import views
from django.urls import path

app_name = 'user_account'
urlpatterns = [
    path('singup', views.singup, name='singup'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),

]