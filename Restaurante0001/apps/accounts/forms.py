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