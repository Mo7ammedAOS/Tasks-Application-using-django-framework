from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.mainHome,name='home'),
    path('adding/',views.addinItems,name='add'),
    path('complete/<int:pk>/',views.taskCompleteness,name='complete'),
    path('dlcompleted/',views.deleteCompleted,name='delcomp'),
    path('dlall/',views.deleteAll,name='delall'),
]
