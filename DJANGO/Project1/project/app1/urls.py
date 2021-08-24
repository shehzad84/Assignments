from django.urls import path
from . import views
urlpatterns = [
    path('greetings/', views.greetings,name="greetings"),
    path('a/',views.hello),
    path('w/',views.welcome),
]