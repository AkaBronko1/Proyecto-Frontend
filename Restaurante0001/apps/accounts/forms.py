from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
import re
from datetime import date, datetime, timedelta

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'tu@email.com o usuario',
            'autocomplete': 'username',
            'id': 'id_username'
        }),
        label='Email o Usuario'
    )
    
    password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Tu contraseña',
            'autocomplete': 'current-password',
            'id': 'id_password'
        }),
        label='Contraseña'
    )
    
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'id': 'remember_me'
        }),
        label='Recordarme en este dispositivo'
    )

    def __init__(self, request=None, *args, **kwargs):
        """Inicializar el formulario con la request para validación"""
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        """Validar las credenciales del usuario"""
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            # Intentar autenticar al usuario
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password
            )
            
            if self.user_cache is None:
                raise ValidationError(
                    'Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.',
                    code='invalid_login'
                )
            elif not self.user_cache.is_active:
                raise ValidationError(
                    'Esta cuenta está desactivada.',
                    code='inactive'
                )

        return cleaned_data

    def get_user(self):
        """Devolver el usuario autenticado"""
        return self.user_cache


class ContactForm(forms.Form):
    """Formulario de contacto para el restaurante"""
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu nombre completo'
        }),
        label='Nombre'
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'tu@email.com'
        }),
        label='Email'
    )
    
    phone = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+34 123 456 789'
        }),
        label='Teléfono (opcional)'
    )
    
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Asunto de tu mensaje'
        }),
        label='Asunto'
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Escribe tu mensaje aquí...'
        }),
        label='Mensaje'
    )

    def clean_phone(self):
        """Validar formato del teléfono"""
        phone = self.cleaned_data.get('phone')
        if phone:
            # Remover espacios y caracteres especiales
            phone = ''.join(filter(str.isdigit, phone))
            if len(phone) < 9:
                raise ValidationError('El teléfono debe tener al menos 9 dígitos.')
            if len(phone) > 15:
                raise ValidationError('El teléfono no puede tener más de 15 dígitos.')
        return phone

    def clean_email(self):
        """Validar formato del email"""
        email = self.cleaned_data.get('email')
        if email:
            # Validación básica de email
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_regex, email):
                raise ValidationError('Por favor ingresa un email válido.')
        return email.lower()


class ReservationForm(forms.Form):
    """Formulario de reservas para el restaurante"""
    PEOPLE_CHOICES = [
        (1, '1 persona'),
        (2, '2 personas'),
        (3, '3 personas'),
        (4, '4 personas'),
        (5, '5 personas'),
        (6, '6 personas'),
        (7, '7 personas'),
        (8, '8 personas'),
        (9, '9+ personas'),
    ]
    
    TIME_CHOICES = [
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('13:00', '13:00'),
        ('13:30', '13:30'),
        ('14:00', '14:00'),
        ('14:30', '14:30'),
        ('20:00', '20:00'),
        ('20:30', '20:30'),
        ('21:00', '21:00'),
        ('21:30', '21:30'),
        ('22:00', '22:00'),
        ('22:30', '22:30'),
    ]
    
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu nombre completo'
        }),
        label='Nombre'
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'tu@email.com'
        }),
        label='Email'
    )
    
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+34 123 456 789'
        }),
        label='Teléfono'
    )
    
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        }),
        label='Fecha de la reserva'
    )
    
    time = forms.ChoiceField(
        choices=TIME_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Hora'
    )
    
    people = forms.ChoiceField(
        choices=PEOPLE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Número de personas'
    )
    
    special_requests = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Solicitudes especiales, alergias, etc. (opcional)'
        }),
        label='Solicitudes especiales'
    )

    def clean_date(self):
        """Validar que la fecha sea futura"""
        fecha = self.cleaned_data.get('date')
        if fecha:
            today = date.today()
            if fecha < today:
                raise ValidationError('La fecha de reserva debe ser hoy o una fecha futura.')
            if fecha > today + timedelta(days=60):
                raise ValidationError('No se pueden hacer reservas con más de 60 días de anticipación.')
        return fecha

    def clean_phone(self):
        """Validar formato del teléfono para reservas"""
        phone = self.cleaned_data.get('phone')
        if phone:
            # Remover espacios y caracteres especiales
            cleaned_phone = ''.join(filter(str.isdigit, phone))
            if len(cleaned_phone) < 9:
                raise ValidationError('El teléfono debe tener al menos 9 dígitos.')
            if len(cleaned_phone) > 15:
                raise ValidationError('El teléfono no puede tener más de 15 dígitos.')
            return phone
        return phone


# ========== FORMULARIOS ADICIONALES PARA ACCOUNTS ==========

class CustomUserCreationForm(UserCreationForm):
    """Formulario personalizado para registro de usuarios"""
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'tu@email.com'
        }),
        label='Correo Electrónico'
    )
    
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Tu nombre'
        }),
        label='Nombre'
    )
    
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Tu apellido'
        }),
        label='Apellido'
    )
    
    phone = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': '+34 123 456 789'
        }),
        label='Teléfono (opcional)'
    )
    
    terms_accepted = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        }),
        label='Acepto los términos y condiciones'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Nombre de usuario'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar widgets de password
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Contraseña'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Confirmar contraseña'
        })

    def clean_email(self):
        """Validar que el email no esté en uso"""
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise ValidationError('Este correo electrónico ya está registrado.')
        return email.lower()

    def clean_username(self):
        """Validar username"""
        username = self.cleaned_data.get('username')
        if username:
            if len(username) < 3:
                raise ValidationError('El nombre de usuario debe tener al menos 3 caracteres.')
            if not re.match("^[a-zA-Z0-9_]+$", username):
                raise ValidationError('El nombre de usuario solo puede contener letras, números y guiones bajos.')
        return username

    def clean_phone(self):
        """Validar teléfono"""
        phone = self.cleaned_data.get('phone')
        if phone:
            cleaned_phone = ''.join(filter(str.isdigit, phone))
            if len(cleaned_phone) < 9:
                raise ValidationError('El teléfono debe tener al menos 9 dígitos.')
        return phone

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    """Formulario para editar perfil de usuario"""
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu apellido'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'tu@email.com'
            })
        }
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico'
        }

    def clean_email(self):
        """Validar email único"""
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError('Este correo electrónico ya está en uso.')
        return email.lower()


class PasswordChangeCustomForm(PasswordChangeForm):
    """Formulario personalizado para cambio de contraseña"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña actual'
        })
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nueva contraseña'
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmar nueva contraseña'
        })

    def clean_new_password1(self):
        """Validar que la nueva contraseña sea segura"""
        password = self.cleaned_data.get('new_password1')
        if password:
            if len(password) < 8:
                raise ValidationError('La contraseña debe tener al menos 8 caracteres.')
            if password.isdigit():
                raise ValidationError('La contraseña no puede ser solo números.')
            if password.lower() in ['password', '12345678', 'qwerty']:
                raise ValidationError('La contraseña es demasiado común.')
        return password


class AccountDeleteForm(forms.Form):
    """Formulario para confirmar eliminación de cuenta"""
    
    confirm_delete = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        }),
        label='Confirmo que deseo eliminar mi cuenta permanentemente'
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu contraseña para confirmar'
        }),
        label='Contraseña actual'
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_password(self):
        """Verificar que la contraseña sea correcta"""
        password = self.cleaned_data.get('password')
        if password and not self.user.check_password(password):
            raise ValidationError('La contraseña ingresada es incorrecta.')
        return password


class NewsletterSubscriptionForm(forms.Form):
    """Formulario para suscripción al newsletter"""
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'tu@email.com'
        }),
        label='Correo Electrónico'
    )
    
    name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu nombre (opcional)'
        }),
        label='Nombre'
    )

    def clean_email(self):
        """Validar formato de email"""
        email = self.cleaned_data.get('email')
        if email:
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_regex, email):
                raise ValidationError('Por favor ingresa un email válido.')
        return email.lower()


class FeedbackForm(forms.Form):
    """Formulario para feedback y sugerencias"""
    
    RATING_CHOICES = [
        (1, '⭐ Muy malo'),
        (2, '⭐⭐ Malo'),
        (3, '⭐⭐⭐ Regular'),
        (4, '⭐⭐⭐⭐ Bueno'),
        (5, '⭐⭐⭐⭐⭐ Excelente'),
    ]
    
    CATEGORY_CHOICES = [
        ('comida', 'Calidad de la comida'),
        ('servicio', 'Atención al cliente'),
        ('entrega', 'Tiempo de entrega'),
        ('web', 'Página web/App'),
        ('otro', 'Otro'),
    ]
    
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu nombre'
        }),
        label='Nombre'
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'tu@email.com'
        }),
        label='Email'
    )
    
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Categoría'
    )
    
    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Calificación'
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Cuéntanos tu experiencia...'
        }),
        label='Mensaje'
    )

    def clean_message(self):
        """Validar longitud del mensaje"""
        message = self.cleaned_data.get('message')
        if message and len(message) < 10:
            raise ValidationError('El mensaje debe tener al menos 10 caracteres.')
        return message