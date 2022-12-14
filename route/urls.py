from django.urls import path

from .import views

urlpatterns = [
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('deposite',views.deposite, name='deposite'),
    path('withdraw',views.withdraw, name='withdraw'),
    path('balance',views.balance, name='balance')
]