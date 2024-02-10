from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'), #empty string means home page
    # name is used to provide an ID

    path('counter', views.counter, name='counter'), # adding a new url 'counter' to the server

    path('register', views.register, name='register'),

    path('login', views.login, name='login'),

    path('logout', views.logout, name='logout'),

    path('post/<str:pk>', views.post, name='post')
]