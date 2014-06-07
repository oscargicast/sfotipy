from django.shortcuts import render
from .forms import UserCreationEmailForm


def signup(request):
    form = UserCreationEmailForm()
    return render(request, 'signup.html', {'form': form})
