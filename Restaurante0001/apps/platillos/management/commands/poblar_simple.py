from django.core.management.base import BaseCommand
from apps.platillos.models import Categoria, Platillo
from decimal import Decimal


class Command(BaseCommand):
    help = 'Crea datos de ejemplo simples para categorías y platillos'

    def handle(self, *args, **options):
        # Limpiar datos existentes
        Platillo.objects.all().delete()
        Categoria.objects.all().delete()
        
        # Crear categorías
        categorias = []
        
        # Entradas
        categoria_entradas = Categoria.objects.create(
            nombre='Entradas',
            descripcion='Perfectas para comenzar tu experiencia gastronómica',
            orden=0,
            activo=True
        )
        categorias.append(categoria_entradas)
        
        # Pizzas
        categoria_pizzas = Categoria.objects.create(
            nombre='Pizzas',
            descripcion='Deliciosas pizzas artesanales con ingredientes frescos',
            orden=1,
            activo=True
        )
        categorias.append(categoria_pizzas)
        
        # Pastas
        categoria_pastas = Categoria.objects.create(
            nombre='Pastas',
            descripcion='Pastas frescas preparadas al momento con salsas caseras',
            orden=2,
            activo=True
        )
        categorias.append(categoria_pastas)
        
        # Ensaladas
        categoria_ensaladas = Categoria.objects.create(
            nombre='Ensaladas',
            descripcion='Ensaladas frescas y nutritivas con ingredientes de temporada',
            orden=3,
            activo=True
        )
        categorias.append(categoria_ensaladas)
        
        # Bebidas
        categoria_bebidas = Categoria.objects.create(
            nombre='Bebidas',
            descripcion='Refrescos naturales, jugos y bebidas calientes',
            orden=4,
            activo=True
        )
        categorias.append(categoria_bebidas)
        
        # Postres
        categoria_postres = Categoria.objects.create(
            nombre='Postres',
            descripcion='Deliciosos postres caseros para cerrar con broche de oro',
            orden=5,
            activo=True
        )
        categorias.append(categoria_postres)
        
        self.stdout.write(f'✅ Creadas {len(categorias)} categorías')
        
        # Crear platillos
        platillos = []
        
        # Entradas
        platillos.append(Platillo.objects.create(
            categoria=categoria_entradas,
            nombre='Bruschetta Italiana',
            descripcion='Pan tostado con tomate fresco, albahaca y aceite de oliva',
            precio=Decimal('85.00'),
            tiempo_preparacion=10,
            calorias=120,
            disponible=True,
            destacado=True,
            vegetariano=True,
            valoracion=Decimal('4.5'),
            numero_valoraciones=23
        ))
        
        platillos.append(Platillo.objects.create(
            categoria=categoria_entradas,
            nombre='Nachos Supremos',
            descripcion='Nachos con queso cheddar, jalapeños, crema ácida y guacamole',
            precio=Decimal('120.00'),
            tiempo_preparacion=15,
            calorias=450,
            disponible=True,
            vegetariano=True,
            picante=True,
            valoracion=Decimal('4.2'),
            numero_valoraciones=18
        ))
        
        # Pizzas
        platillos.append(Platillo.objects.create(
            categoria=categoria_pizzas,
            nombre='Pizza Margherita',
            descripcion='Salsa de tomate, mozzarella fresca, albahaca y aceite de oliva',
            precio=Decimal('185.00'),
            tiempo_preparacion=20,
            calorias=580,
            disponible=True,
            destacado=True,
            vegetariano=True,
            valoracion=Decimal('4.8'),
            numero_valoraciones=67
        ))
        
        platillos.append(Platillo.objects.create(
            categoria=categoria_pizzas,
            nombre='Pizza Pepperoni',
            descripcion='Salsa de tomate, mozzarella y abundante pepperoni',
            precio=Decimal('210.00'),
            tiempo_preparacion=22,
            calorias=720,
            disponible=True,
            destacado=True,
            valoracion=Decimal('4.6'),
            numero_valoraciones=54
        ))
        
        platillos.append(Platillo.objects.create(
            categoria=categoria_pizzas,
            nombre='Pizza Hawaiana',
            descripcion='Salsa de tomate, mozzarella, jamón y piña natural',
            precio=Decimal('195.00'),
            tiempo_preparacion=20,
            calorias=650,
            disponible=True,
            valoracion=Decimal('4.1'),
            numero_valoraciones=31
        ))
        
        # Pastas
        platillos.append(Platillo.objects.create(
            categoria=categoria_pastas,
            nombre='Spaghetti Carbonara',
            descripcion='Pasta con salsa cremosa de huevo, panceta y parmesano',
            precio=Decimal('165.00'),
            tiempo_preparacion=18,
            calorias=620,
            disponible=True,
            destacado=True,
            valoracion=Decimal('4.7'),
            numero_valoraciones=38
        ))
        
        platillos.append(Platillo.objects.create(
            categoria=categoria_pastas,
            nombre='Penne Arrabbiata',
            descripcion='Pasta con salsa de tomate picante, ajo y perejil',
            precio=Decimal('145.00'),
            tiempo_preparacion=15,
            calorias=520,
            disponible=True,
            vegetariano=True,
            vegano=True,
            picante=True,
            valoracion=Decimal('4.3'),
            numero_valoraciones=29
        ))
        
        platillos.append(Platillo.objects.create(
            categoria=categoria_pastas,
            nombre='Lasaña de la Casa',
            descripcion='Capas de pasta con carne molida, bechamel y queso gratinado',
            precio=Decimal('195.00'),
            tiempo_preparacion=35,
            calorias=850,
            disponible=True,
            destacado=True,
            valoracion=Decimal('4.9'),
            numero_valoraciones=72
        ))
        
        # Ensaladas
        platillos.append(Platillo.objects.create(
            categoria=categoria_ensaladas,
            nombre='Ensalada César',
            descripcion='Lechuga romana, crutones, parmesano y aderezo césar',
            precio=Decimal('125.00'),
            tiempo_preparacion=10,
            calorias=320,
            disponible=True,
            vegetariano=True,
            valoracion=Decimal('4.2'),
            numero_valoraciones=26
        ))
        
        platillos.append(Platillo.objects.create(
            categoria=categoria_ensaladas,
            nombre='Ensalada Griega',
            descripcion='Tomate, pepino, cebolla, aceitunas, queso feta y vinagreta',
            precio=Decimal('135.00'),
            tiempo_preparacion=8,
            calorias=280,
            disponible=True,
            vegetariano=True,
            sin_gluten=True,
            valoracion=Decimal('4.0'),
            numero_valoraciones=19
        ))
        
        # Bebidas
        platillos.append(Platillo.objects.create(
            categoria=categoria_bebidas,
            nombre='Agua Fresca de Jamaica',
            descripcion='Bebida refrescante natural de flor de jamaica',
            precio=Decimal('35.00'),
            tiempo_preparacion=2,
            calorias=45,
            disponible=True,
            vegetariano=True,
            vegano=True,
            sin_gluten=True,
            valoracion=Decimal('4.3'),
            numero_valoraciones=15
        ))
        
        platillos.append(Platillo.objects.create(
            categoria=categoria_bebidas,
            nombre='Smoothie de Fresa',
            descripcion='Batido natural con fresas frescas, yogurt y miel',
            precio=Decimal('65.00'),
            tiempo_preparacion=5,
            calorias=180,
            disponible=True,
            destacado=True,
            vegetariano=True,
            sin_gluten=True,
            valoracion=Decimal('4.6'),
            numero_valoraciones=21
        ))
        
        # Postres
        platillos.append(Platillo.objects.create(
            categoria=categoria_postres,
            nombre='Tiramisú',
            descripcion='El clásico postre italiano con café, mascarpone y cacao',
            precio=Decimal('95.00'),
            tiempo_preparacion=15,
            calorias=420,
            disponible=True,
            destacado=True,
            vegetariano=True,
            valoracion=Decimal('4.8'),
            numero_valoraciones=44
        ))
        
        platillos.append(Platillo.objects.create(
            categoria=categoria_postres,
            nombre='Helado Artesanal',
            descripcion='Helado casero disponible en vainilla, chocolate y fresa',
            precio=Decimal('55.00'),
            tiempo_preparacion=3,
            calorias=220,
            disponible=True,
            vegetariano=True,
            sin_gluten=True,
            valoracion=Decimal('4.2'),
            numero_valoraciones=28
        ))
        
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