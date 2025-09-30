from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def main_index(request):
    return render(request, 'main/index.html')

@login_required(login_url='accounts:login')
def index_user(request):
    return render(request, 'main/main_index.html')