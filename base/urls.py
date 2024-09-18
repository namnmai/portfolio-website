from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('contact/', views.contactPage, name='contact'),
    path('contact/success/', views.contactSuccess, name='contact_success'),
    path('project/<str:pk>/', views.projectPage, name="project"),
    path('inbox/', views.inboxPage, name="inbox"),
    path('message/<str:pk>/', views.messagePage, name="message")
]