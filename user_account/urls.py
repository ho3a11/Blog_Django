from . import views
from django.urls import path

app_name = 'user_account' # Defines the application namespace for this set of URLs.
urlpatterns = [ # Defines URL patterns for the user account application.
    path('singup', views.singup, name='singup'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),

]