from django.core.management.base import BaseCommand
from apps.platillos.models import Categoria, Platillo
from decimal import Decimal


class Command(BaseCommand):
    help = 'Crea datos de ejemplo para categorías y platillos'

    def handle(self, *args, **options):
        # Limpiar datos existentes
        Platillo.objects.all().delete()
        Categoria.objects.all().delete()
        
        # Crear categorías
        categorias_data = [
            {
                'nombre': 'Pizzas',
                'descripcion': 'Deliciosas pizzas artesanales con ingredientes frescos',
                'orden': 1,
                'activo': True
            },
            {
                'nombre': 'Pastas',
                'descripcion': 'Pastas frescas preparadas al momento con salsas caseras',
                'orden': 2,
                'activo': True
            },
            {
                'nombre': 'Ensaladas',
                'descripcion': 'Ensaladas frescas y nutritivas con ingredientes de temporada',
                'orden': 3,
                'activo': True
            },
            {
                'nombre': 'Bebidas',
                'descripcion': 'Refrescos naturales, jugos y bebidas calientes',
                'orden': 4,
                'activo': True
            },
            {
                'nombre': 'Postres',
                'descripcion': 'Deliciosos postres caseros para cerrar con broche de oro',
                'orden': 5,
                'activo': True
            },
            {
                'nombre': 'Entradas',
                'descripcion': 'Perfectas para comenzar tu experiencia gastronómica',
                'orden': 0,
                'activo': True
            }
        ]
        
        categorias = {}
        for cat_data in categorias_data:
            categoria = Categoria.objects.create(**cat_data)
            categorias[cat_data['nombre']] = categoria
            self.stdout.write(f'✅ Categoría creada: {categoria.nombre}')
        
        # Crear platillos
        platillos_data = [
            # Entradas
            {
                'categoria': 'Entradas',
                'nombre': 'Bruschetta Italiana',
                'descripcion': 'Pan tostado con tomate fresco, albahaca y aceite de oliva',
                'precio': Decimal('85.00'),
                'tiempo_preparacion': 10,
                'calorias': 120,
                'disponible': True,
                'destacado': True,
                'vegetariano': True,
                'valoracion': Decimal('4.5'),
                'numero_valoraciones': 23
            },
            {
                'categoria': 'Entradas',
                'nombre': 'Nachos Supremos',
                'descripcion': 'Nachos con queso cheddar, jalapeños, crema ácida y guacamole',
                'precio': Decimal('120.00'),
                'tiempo_preparacion': 15,
                'calorias': 450,
                'disponible': True,
                'destacado': False,
                'vegetariano': True,
                'picante': True,
                'valoracion': Decimal('4.2'),
                'numero_valoraciones': 18
            },
            
            # Pizzas
            {
                'categoria': 'Pizzas',
                'nombre': 'Pizza Margherita',
                'descripcion': 'Salsa de tomate, mozzarella fresca, albahaca y aceite de oliva',
                'precio': Decimal('185.00'),
                'tiempo_preparacion': 20,
                'calorias': 580,
                'disponible': True,
                'destacado': True,
                'vegetariano': True,
                'rating': 4.8,
                'numero_valoraciones': 67,
                'vistas': 245
            },
            {
                'categoria': 'Pizzas',
                'nombre': 'Pizza Pepperoni',
                'descripcion': 'Salsa de tomate, mozzarella y abundante pepperoni',
                'precio': Decimal('210.00'),
                'tiempo_preparacion': 22,
                'calorias': 720,
                'disponible': True,
                'destacado': True,
                'rating': 4.6,
                'numero_valoraciones': 54,
                'vistas': 198
            },
            {
                'categoria': 'Pizzas',
                'nombre': 'Pizza Hawaiana',
                'descripcion': 'Salsa de tomate, mozzarella, jamón y piña natural',
                'precio': Decimal('195.00'),
                'tiempo_preparacion': 20,
                'calorias': 650,
                'disponible': True,
                'destacado': False,
                'rating': 4.1,
                'numero_valoraciones': 31,
                'vistas': 132
            },
            {
                'categoria': 'Pizzas',
                'nombre': 'Pizza Cuatro Quesos',
                'descripcion': 'Mozzarella, parmesano, gorgonzola y ricotta',
                'precio': Decimal('230.00'),
                'tiempo_preparacion': 25,
                'calorias': 780,
                'disponible': True,
                'destacado': False,
                'vegetariano': True,
                'rating': 4.4,
                'numero_valoraciones': 42,
                'vistas': 167
            },
            
            # Pastas
            {
                'categoria': 'Pastas',
                'nombre': 'Spaghetti Carbonara',
                'descripcion': 'Pasta con salsa cremosa de huevo, panceta y parmesano',
                'precio': Decimal('165.00'),
                'tiempo_preparacion': 18,
                'calorias': 620,
                'disponible': True,
                'destacado': True,
                'rating': 4.7,
                'numero_valoraciones': 38,
                'vistas': 189
            },
            {
                'categoria': 'Pastas',
                'nombre': 'Penne Arrabbiata',
                'descripcion': 'Pasta con salsa de tomate picante, ajo y perejil',
                'precio': Decimal('145.00'),
                'tiempo_preparacion': 15,
                'calorias': 520,
                'disponible': True,
                'destacado': False,
                'vegetariano': True,
                'vegano': True,
                'picante': True,
                'rating': 4.3,
                'numero_valoraciones': 29,
                'vistas': 98
            },
            {
                'categoria': 'Pastas',
                'nombre': 'Lasaña de la Casa',
                'descripcion': 'Capas de pasta con carne molida, bechamel y queso gratinado',
                'precio': Decimal('195.00'),
                'tiempo_preparacion': 35,
                'calorias': 850,
                'disponible': True,
                'destacado': True,
                'rating': 4.9,
                'numero_valoraciones': 72,
                'vistas': 234
            },
            
            # Ensaladas
            {
                'categoria': 'Ensaladas',
                'nombre': 'Ensalada César',
                'descripcion': 'Lechuga romana, crutones, parmesano y aderezo césar',
                'precio': Decimal('125.00'),
                'tiempo_preparacion': 10,
                'calorias': 320,
                'disponible': True,
                'destacado': False,
                'vegetariano': True,
                'rating': 4.2,
                'numero_valoraciones': 26,
                'vistas': 87
            },
            {
                'categoria': 'Ensaladas',
                'nombre': 'Ensalada Griega',
                'descripcion': 'Tomate, pepino, cebolla, aceitunas, queso feta y vinagreta',
                'precio': Decimal('135.00'),
                'tiempo_preparacion': 8,
                'calorias': 280,
                'disponible': True,
                'destacado': False,
                'vegetariano': True,
                'sin_gluten': True,
                'rating': 4.0,
                'numero_valoraciones': 19,
                'vistas': 63
            },
            
            # Bebidas
            {
                'categoria': 'Bebidas',
                'nombre': 'Agua Fresca de Jamaica',
                'descripcion': 'Bebida refrescante natural de flor de jamaica',
                'precio': Decimal('35.00'),
                'tiempo_preparacion': 2,
                'calorias': 45,
                'disponible': True,
                'destacado': False,
                'vegetariano': True,
                'vegano': True,
                'sin_gluten': True,
                'rating': 4.3,
                'numero_valoraciones': 15,
                'vistas': 78
            },
            {
                'categoria': 'Bebidas',
                'nombre': 'Café Americano',
                'descripcion': 'Café espresso con agua caliente, servido en taza grande',
                'precio': Decimal('45.00'),
                'tiempo_preparacion': 5,
                'calorias': 5,
                'disponible': True,
                'destacado': False,
                'vegetariano': True,
                'vegano': True,
                'sin_gluten': True,
                'rating': 4.1,
                'numero_valoraciones': 12,
                'vistas': 56
            },
            {
                'categoria': 'Bebidas',
                'nombre': 'Smoothie de Fresa',
                'descripcion': 'Batido natural con fresas frescas, yogurt y miel',
                'precio': Decimal('65.00'),
                'tiempo_preparacion': 5,
                'calorias': 180,
                'disponible': True,
                'destacado': True,
                'vegetariano': True,
                'sin_gluten': True,
                'rating': 4.6,
                'numero_valoraciones': 21,
                'vistas': 94
            },
            
            # Postres
            {
                'categoria': 'Postres',
                'nombre': 'Tiramisú',
                'descripcion': 'El clásico postre italiano con café, mascarpone y cacao',
                'precio': Decimal('95.00'),
                'tiempo_preparacion': 15,
                'calorias': 420,
                'disponible': True,
                'destacado': True,
                'vegetariano': True,
                'rating': 4.8,
                'numero_valoraciones': 44,
                'vistas': 178
            },
            {
                'categoria': 'Postres',
                'nombre': 'Cheesecake de Fresa',
                'descripcion': 'Cremoso cheesecake con mermelada casera de fresa',
                'precio': Decimal('85.00'),
                'tiempo_preparacion': 10,
                'calorias': 380,
                'disponible': True,
                'destacado': False,
                'vegetariano': True,
                'rating': 4.4,
                'numero_valoraciones': 33,
                'vistas': 112
            },
            {
                'categoria': 'Postres',
                'nombre': 'Helado Artesanal',
                'descripcion': 'Helado casero disponible en vainilla, chocolate y fresa',
                'precio': Decimal('55.00'),
                'tiempo_preparacion': 3,
                'calorias': 220,
                'disponible': True,
                'destacado': False,
                'vegetariano': True,
                'sin_gluten': True,
                'rating': 4.2,
                'numero_valoraciones': 28,
                'vistas': 89
            }
        ]
        
        for platillo_data in platillos_data:
            categoria_nombre = platillo_data.pop('categoria')
            platillo_data['categoria'] = categorias[categoria_nombre]
            
            platillo = Platillo.objects.create(**platillo_data)
            self.stdout.write(f'✅ Platillo creado: {platillo.nombre} ({categoria_nombre})')
        
        # Estadísticas finales
        total_categorias = Categoria.objects.count()
        total_platillos = Platillo.objects.count()
        platillos_destacados = Platillo.objects.filter(destacado=True).count()
        platillos_vegetarianos = Platillo.objects.filter(vegetariano=True).count()
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\n🎉 ¡Base de datos poblada exitosamente!\n'
                f'📁 Categorías creadas: {total_categorias}\n'
                f'🍽️ Platillos creados: {total_platillos}\n'
                f'⭐ Platillos destacados: {platillos_destacados}\n'
                f'🌱 Platillos vegetarianos: {platillos_vegetarianos}\n'
            )
        )