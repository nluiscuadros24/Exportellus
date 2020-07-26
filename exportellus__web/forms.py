from django import forms

#from django.contrib.auth.models import User
from users.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'username'
                                }))
    email = forms.EmailField(required=True,
                                widget=forms.EmailInput(attrs={
                                    'class': 'form-control',
                                    'id': 'email',
                                    'placeholder': 'example@exportellus.com'
                                }))
    password = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control'
                                }))
    password2 = forms.CharField(label='Confirmar password',
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control'
                                }))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')

        return email

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'El password no coincide')

    def save(self):
        return User.objects.create_user(
                self.cleaned_data.get('username'),
                self.cleaned_data.get('email'),
                self.cleaned_data.get('password'),
            )

#class UpdateProfileForm(forms.Form):
    #Title = forms.CharField(required=True,
                                #min_length=4, max_length=50,
                                #widget=forms.TextInput(attrs={
                                    #'class': 'form-control',
                                    #'id': 'Título'
                                #}))
    #Descripción = forms.CharField(required=True,
                                #min_length=4, max_length=200,
                                #widget=forms.TextInput(attrs={
                                    #'class': 'form-control',
                                    #'id': 'Descripcion',
                                #}))
    #Precio = forms.DecimalField(required=True,
                                #max_digits=8, decimal_places=2, default=0.0,
                                #widget=forms.NumberInput(attrs={
                                    #'class': 'form-control',
                                    #'id': 'Precio',
                                #}))
    #Slug = forms.SlugField(required=True,
                                #null=False, blank=False, unique=True,
                                #widget=forms.TextInput(attrs={
                                    #'class': 'form-control',
                                    #'id': '',
                                #}))
    #Imagenes = forms.ImageField(required=True,
                                #upload_to='products/', null=False, blank=False,
                                #widget=forms.ClearableFileInput(attrs={
                                    #'class': 'form-control',
                                    #'id': '',
                                #}))
    #created_at = forms.DateTimeField(required=True,
                                #auto_now_add=True,
                                #widget=forms.DateTimeInput(attrs={
                                    #'class': 'form-control',
                                    #'id': '',
                                #}))


