"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.homepage),
    path('home', views.homepage),
    path('admin/', admin.site.urls),
    path('sign-in', views.sign_in),
    path('book-entry', views.book_entry),
    path('book-view', views.book_entry),
    path('book-view-update/<int:id>/', views.bookviewupdate),
    path('book-view-delete/<int:id>/', views.bookviewdelete),
    path('book-details/<int:id>/', views.bookdetails),
    path('create-account', views.create_account),
    path('client-home', views.client_home),
    path('magazine-entry', views.magazine_entry),
    path('magazine-view-update/<int:id>/', views.magazineviewupdate),
    path('magazine-view-delete/<int:id>/', views.magazineviewdelete),
    path('magazine-details/<int:id>/', views.magazinedetails),
    path('video-entry', views.video_entry),
    path('admin-dashboard', views.admin_dashboard),
    path('active-users', views.active_users),
    path('video-view-update/<int:id>/', views.videoviewupdate),
    path('video-view-delete/<int:id>/', views.videoviewdelete),
    path('video-details/<int:id>/', views.videodetails),
    path('music-entry', views.music_entry),
    path('music-view-update/<int:id>/', views.musicviewupdate),
    path('music-view-delete/<int:id>/', views.musicviewdelete),
    path('music-details/<int:id>/', views.musicdetails),
    path('register-admin', views.register_admin),
    path('book-list', views.booklist),
    path('video-list', views.videolist),
    path('magazine-list', views.magazinelist),
    path('music-list', views.musiclist),
    path('view-All', views.view_All),
    path('catalogue', views.catalogview),
    path('book-search', views.booksearch),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
