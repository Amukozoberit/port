from django.urls import path
from . import views
urlpatterns = [
    
path('',views.picture_image,name='picture_image'),
]