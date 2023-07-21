from django.urls import path
from mainapp.views import profile_view

app_name = "mainapp"

urlpatterns = [
    path('', profile_view, name = 'profile'),

]
