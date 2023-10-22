
from homePage import views 
from django.urls import path 

urlpatterns = [
    path('', views.homes, name = 'homes'),
    path('delete/<task_id>', views.delete, name = 'delete'),
    path('edit/<task_id>',views.edit,name = 'edit'),
    path('complete/<task_id>',views.complete, name = 'complete'),
    path('Notcomplete/<task_id>',views.notcomplete, name = 'notcomplete'),
    path('contact', views.contact, name='contact'),
    path('about',views.about,name='about'),
  
]
