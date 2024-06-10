"""
URL configuration for library_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from library import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/<int:book_id>/', views.book_detail_view, name='book_detail'),
    path('author/<int:author_id>/', views.author_detail_view, name='author_detail'),
    path('genres/', views.genre_list_view, name='genre_list'),
    path('home/', views.home_view, name='home'),
    path('book/<int:book_id>/update/', views.update_book, name='update_book'),
    path('book/<int:book_id>/remove_genre/', views.remove_genre_from_book, name='remove_genre_from_book'),
    path('book/login/',views.user_login,name ='user_login'),
    path('book/register/', views.register, name ='register'),
    path('book/protected/',views.protected_view,name='protected'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.user_logout, name='logout'),
]
