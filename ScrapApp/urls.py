from django.contrib import admin
from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index, name='index'),
    url(r'^$',views.webscrip,name='webscrip'),
    url(r'webscripimage',views.webscripimage,name='webscripimage'),
]