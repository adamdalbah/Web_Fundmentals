from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ),
    path('reset', views.reset),
    path('add2',views.add2),
    path('increment',views.increment)

]