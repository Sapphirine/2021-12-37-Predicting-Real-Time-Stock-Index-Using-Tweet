from django.conf.urls import url
from django.urls import path
from posts import views
 
urlpatterns = [
    path('hello/', views.hello),
    path('dashboard/', views.dashboard),
    path('connection/', views.connection),
    path('overview/', views.overview)
]