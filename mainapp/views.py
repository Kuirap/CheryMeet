from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from mainapp.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate
from mainapp.forms import LoginForm
from django.contrib.auth.decorators import login_required


@login_required 
def profile_view(request):

    return render(request, "web/profile.html")

