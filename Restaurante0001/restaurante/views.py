from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, Sum

def index_user(request):
    """Página principal simple como en el proyecto de referencia"""
    return render(request, 'main/base_user.html')

def landing_page(request):
    """Landing page para usuarios no autenticados"""
    if request.user.is_authenticated:
        return redirect('main:index')
    return render(request, 'main/landing.html')

@login_required
def dashboard(request):
    """Dashboard para usuarios autenticados"""
    # Importar modelos de platillos
    try:
        from apps.platillos.models import Categoria, Platillo
        
        # Estadísticas
        categorias_count = Categoria.objects.count()
        platillos_count = Platillo.objects.count()
        promedio_rating = Platillo.objects.aggregate(
            promedio=Avg('valoracion')
        )['promedio'] or 0.0
        # Sumar el total de valoraciones de todos los platillos
        total_valoraciones = Platillo.objects.aggregate(
            total=Sum('numero_valoraciones')
        )['total'] or 0
        
        # Platillos recientes (últimos 5)
        recent_platillos = Platillo.objects.order_by('-id')[:5]
        
        context = {
            'categorias_count': categorias_count,
            'platillos_count': platillos_count,
            'promedio_rating': round(promedio_rating, 1),
            'total_vistas': total_valoraciones,
            'recent_platillos': recent_platillos,
        }
        
    except ImportError:
        # Si los modelos no están disponibles, usar valores por defecto
        context = {
            'categorias_count': 0,
            'platillos_count': 0,
            'promedio_rating': 0.0,
            'total_vistas': 0,
            'recent_platillos': [],
        }
    
    return render(request, 'main/dashboard.html', context)

@login_required
def main_index(request):
    """Página principal/index para usuarios autenticados"""
    # Importar modelos de platillos
    try:
        from apps.platillos.models import Categoria, Platillo
        
        # Estadísticas básicas
        categorias_count = Categoria.objects.count()
        platillos_count = Platillo.objects.count()
        promedio_rating = Platillo.objects.aggregate(
            promedio=Avg('valoracion')
        )['promedio'] or 0.0
        # Sumar el total de valoraciones de todos los platillos
        total_valoraciones = Platillo.objects.aggregate(
            total=Sum('numero_valoraciones')
        )['total'] or 0
        
        # Platillos recientes (últimos 3 para el index)
        recent_platillos = Platillo.objects.order_by('-id')[:3]
        
        context = {
            'categorias_count': categorias_count,
            'platillos_count': platillos_count,
            'promedio_rating': round(promedio_rating, 1),
            'total_vistas': total_valoraciones,
            'recent_platillos': recent_platillos,
        }
        
    except ImportError:
        # Si los modelos no están disponibles, usar valores por defecto
        context = {
            'categorias_count': 0,
            'platillos_count': 0,
            'promedio_rating': 0.0,
            'total_vistas': 0,
            'recent_platillos': [],
        }
    
    return render(request, 'main/main_index.html', context)