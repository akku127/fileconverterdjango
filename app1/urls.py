from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('docxhandler/', views.docxtopdf, name='docxfile'),
    path('jpghandler/', views.jpgtopng, name='jpgfile'),
    path('converter1/', views.converter1, name='convertdocx'),
    path('converter2/', views.converter2, name='convertjpg'),
    path('wait/', views.wait, name='wait'),
]