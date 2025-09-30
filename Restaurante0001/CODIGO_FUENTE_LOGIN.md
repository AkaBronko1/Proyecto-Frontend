# 📁 CÓDIGO FUENTE - ARCHIVOS PRINCIPALES

## **1. MODELO DE USUARIO**

### **Archivo**: `apps/accounts/models.py`

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class AppUser(AbstractUser):
    pass
```

---

## **2. FORMULARIO DE LOGIN**

### **Archivo**: `apps/accounts/forms.py`

```python
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario',
                max_length=150, required=True, 
                widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True)
    remember_me = forms.BooleanField(
        label='Recordar mis datos', 
        required=False, initial=False, 
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
```

---

## **3. VISTAS DE AUTENTICACIÓN**

### **Archivo**: `apps/accounts/views.py`

```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from .models import AppUser
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Aquí iría la lógica de autenticación del usuario
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']
            # Autenticación y redirección según sea necesario
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                
                # Redirigir a la página principal o a la que corresponda
                return redirect('index_user')
            else:
                form.add_error(None, 'Credenciales inválidas')
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('main_index')

class UserListView(LoginRequiredMixin, ListView):
    login_url = 'accounts:login'
    model = AppUser
    template_name = 'accounts/user_list.html'
    context_object_name = 'users'
```

---

## **4. VISTA PROTEGIDA**

### **Archivo**: `restaurante/views.py`

```python
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def main_index(request):
    return render(request, 'main/index.html')

@login_required(login_url='accounts:login')
def index_user(request):
    return render(request, 'main/main_index.html')
```

---

## **5. CONFIGURACIÓN DE URLS**

### **Archivo**: `apps/accounts/urls.py`

```python
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.UserListView.as_view(), name='user_list'),
]
```

### **Archivo**: `restaurante/urls.py`

```python
"""
URL configuration for restaurante project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_index, name='main_index'),
    path('accounts/', include('apps.accounts.urls')),
    path('platillos/', include('apps.platillos.urls')),
    path('dashboard/', views.index_user, name='index_user'),
]
```

---

## **6. CONFIGURACIÓN DE APLICACIÓN**

### **Archivo**: `apps/accounts/apps.py`

```python
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'
```

---

## **7. CONFIGURACIÓN DE SETTINGS**

### **Archivo**: `restaurante/settings.py` (fragmentos relevantes)

```python
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Local apps
    'apps.accounts',
    'apps.platillos',
]

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Custom User Model
AUTH_USER_MODEL = 'accounts.AppUser'
```

---

## **8. TEMPLATE DE LOGIN**

### **Archivo**: `templates/accounts/login.html` (fragmento principal)

```html
{% extends 'main/base.html' %}

{% block extra_head %}
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css">
<style>
    body {
        background-color: #f8f9fa;
        height: 100vh;
        display: flex;
        align-items: center;
    }
    .login-container {
        max-width: 400px;
        width: 100%;
    }
</style>
{% endblock %}

{% block content %}
<div class="login-container">
    <div class="card shadow-lg border-0">
        <div class="card-header bg-warning text-dark text-center py-4">
            <h3 class="mb-0 fw-bold">
                <i class="bi bi-pizza me-2"></i>
                Iniciar Sesión
            </h3>
        </div>
        
        <div class="card-body p-5">
            <!-- Mensajes de error -->
            {% if form.errors %}
                <div class="alert alert-danger d-flex align-items-center">
                    <i class="bi bi-exclamation-triangle me-2"></i>
                    <div>
                        <strong>Error:</strong> Por favor corrige los errores.
                    </div>
                </div>
            {% endif %}

            <!-- Formulario de Login -->
            <form method="post" novalidate>
                {% csrf_token %}
                
                <!-- Campo Usuario -->
                <div class="mb-4">
                    <label for="id_username" class="form-label fw-semibold">
                        <i class="bi bi-person me-1"></i>Email o Usuario
                    </label>
                    <input 
                        type="text" 
                        class="form-control form-control-lg" 
                        id="id_username" 
                        name="username" 
                        value="{{ form.username.value|default:'' }}"
                        placeholder="tu@email.com"
                        required
                    >
                </div>

                <!-- Campo Contraseña -->
                <div class="mb-4">
                    <label for="id_password" class="form-label fw-semibold">
                        <i class="bi bi-lock me-1"></i>Contraseña
                    </label>
                    <input 
                        type="password" 
                        class="form-control form-control-lg" 
                        id="id_password" 
                        name="password"
                        placeholder="Tu contraseña"
                        required
                    >
                </div>

                <!-- Checkbox Recordar -->
                <div class="form-check mb-4">
                    <input 
                        type="checkbox" 
                        class="form-check-input" 
                        id="id_remember_me" 
                        name="remember_me"
                    >
                    <label class="form-check-label" for="id_remember_me">
                        Recordar mis datos
                    </label>
                </div>

                <!-- Botón Submit -->
                <button type="submit" class="btn btn-warning btn-lg w-100 mb-4">
                    <i class="bi bi-box-arrow-in-right me-2"></i>
                    Iniciar Sesión
                </button>
            </form>
        </div>
    </div>
</div>
{% endblock %}
```

---

## **9. TEMPLATE BASE**

### **Archivo**: `templates/main/base.html` (fragmento principal)

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Restaurante</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">

    <style>
        .hero-section {
            background-color: #f8f9fa;
            padding: 100px 0;
            text-align: center;
        }
        .nav-link {
            color: #495057;
            font-weight: 500;
        }
        .nav-link:hover {
            color: #000;
        }
    </style>

    {% block extra_head %}
    {% endblock %}
</head>
<body>
    {% block content %}
    {% endblock %}

    <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
</body>
</html>
```

---

## **10. TEMPLATE DASHBOARD**

### **Archivo**: `templates/main/main_index.html` (fragmento principal)

```html
{% extends 'main/base_user.html' %}

{% block content %}
<div class="row mb-4">
    <div class="col-12">
        <h2 class="mb-4">Dashboard</h2>
        
        <!-- Stats Cards -->
        <div class="row g-4 mb-4">
            <div class="col-md-3">
                <div class="stat-card card bg-white">
                    <div class="card-body">
                        <div class="d-flex justify-content-between align-items-center">
                            <div>
                                <h6 class="card-subtitle mb-1 text-muted">Ventas Hoy</h6>
                                <h3 class="card-title">$1,245.80</h3>
                                <p class="card-text small text-success">
                                    <i class="bi bi-arrow-up"></i> 12% desde ayer
                                </p>
                            </div>
                            <div class="card-icon text-primary">
                                <i class="bi bi-currency-dollar"></i>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Más cards de estadísticas... -->
        </div>
    </div>
</div>
{% endblock %}
```

---

## **📊 RESUMEN DE ARCHIVOS MODIFICADOS/CREADOS**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `apps/accounts/models.py` | **Modelo** | Usuario personalizado |  
| `apps/accounts/forms.py` | **Formulario** | LoginForm con validación |
| `apps/accounts/views.py` | **Vista** | login_view, logout_view |
| `apps/accounts/urls.py` | **URLs** | Rutas de autenticación |
| `apps/accounts/apps.py` | **Config** | Configuración de la app |
| `restaurante/views.py` | **Vista** | Vista protegida con @login_required |
| `restaurante/urls.py` | **URLs** | URLs principales del proyecto |
| `restaurante/settings.py` | **Config** | AUTH_USER_MODEL, INSTALLED_APPS |
| `templates/accounts/login.html` | **Template** | Formulario de login |
| `templates/main/base.html` | **Template** | Template base público |
| `templates/main/main_index.html` | **Template** | Dashboard protegido |

---

*Este código fuente demuestra la implementación completa del sistema de autenticación con Django 5.2.5*