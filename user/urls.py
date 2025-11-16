from django.urls import path
from .import views

urlpatterns = [
   path('',views.create,name='create'),
   path('list/',views.read,name='list'),
   path('user/details/<int:pk>/',views.details,name='details'),
   path('user/<int:pk>/update/',views.update,name='update'),
   path('user/<int:pk>/delete/',views.delete,name='delete')
]