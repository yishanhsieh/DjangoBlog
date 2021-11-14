"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib import admin
#from trips.views import hello_world, home, post_detail
from myblog.views import HomeView, ArticleDetailView, AddPostView, bloghome2, about


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^hello/$', hello_world),
    #url(r'^$', home),
    #url(r'^post/(?P<pk>\d+)/$', post_detail,name='post_detail'),
    #url(r'^bloghome/$', bloghome),
    url(r'^$', bloghome2, name='home'),
    url(r'^about$', about, name='about'),
    #path('', HomeView.as_view(), name='home'),
    #path('article/<int:pk>',ArticleDetailView.as_view(), name='article-detail'),
    #path('add_post/', AddPostView.as_view(), name = 'add_post'),
    url(r'mdeditor/', include('mdeditor.urls')),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='post_detail'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

