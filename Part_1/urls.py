from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.index),
    path('greet/',views.greet),
    path('rec/',views.rec),
    path('xyz/',views.xyz),
    path('abc/',views.abc),
    path('de/',views.de),
    path('fg/',views.fg),
    path('hij/',views.hij),
    path('home/',views.home),
]
