from django.urls import path
from . import views
urlpatterns = [
    path('Inscription',views.inscriptionPage,name='inscription'),
    path('acces',views.accesPage,name='acces'),
    path('quitter',views.logoutUser,name='quitter'),
]
