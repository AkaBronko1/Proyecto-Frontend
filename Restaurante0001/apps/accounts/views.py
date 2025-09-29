from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse


def index(request):
    return HttpResponse("Accounts app is up!")
    
class CustomLoginView(LoginView):
    """Vista personalizada para el login"""
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('main:index')  # Redirige al index principal
    redirect_authenticated_user = True
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesión - Pizza Moderna'
        return context
    
    def form_valid(self, form):
        """Se ejecuta cuando el formulario es válido"""
        remember_me = self.request.POST.get('remember_me')
        
        if not remember_me:
            # Si no marca "recordarme", la sesión expira al cerrar el navegador
            self.request.session.set_expiry(0)
        else:
            # Si marca "recordarme", la sesión dura 30 días
            self.request.session.set_expiry(30 * 24 * 60 * 60)
        
        messages.success(self.request, f'¡Bienvenido de vuelta, {form.get_user().first_name or form.get_user().username}!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario tiene errores"""
        messages.error(self.request, 'Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.')
        return super().form_invalid(form)


def logout_view(request):
    """Vista de logout usando función"""
    logout(request)
    messages.success(request, '¡Has cerrado sesión correctamente! Te esperamos pronto.')
    return redirect('main:landing')


def login_view(request):
    """Vista alternativa de login usando función (si prefieres no usar clases)"""
    if request.user.is_authenticated:
        return redirect('main:index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                # Manejar "recordarme"
                if not remember_me:
                    request.session.set_expiry(0)
                else:
                    request.session.set_expiry(30 * 24 * 60 * 60)
                
                messages.success(request, f'¡Bienvenido de vuelta, {user.first_name or user.username}!')
                
                # Redirigir a la página solicitada o al index principal
                next_url = request.GET.get('next', 'main:index')
                return redirect(next_url)
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Por favor completa todos los campos.')
    
    return render(request, 'accounts/login.html')


@login_required
def profile_view(request):
    """Vista del perfil del usuario (requiere login)"""
    context = {
        'user': request.user,
        'title': 'Mi Perfil - Pizza Moderna'
    }
    return render(request, 'accounts/profile.html', context)


def register_view(request):
    """Vista de registro de nuevos usuarios"""
    if request.user.is_authenticated:
        return redirect('main:index')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada exitosamente para {username}! Ya puedes iniciar sesión.')
            return redirect('accounts:login')
        else:
            messages.error(request, 'Hubo errores en el formulario. Por favor revisa los datos.')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form,
        'title': 'Crear Cuenta - Pizza Moderna'
    }
    return render(request, 'accounts/register.html', context)
