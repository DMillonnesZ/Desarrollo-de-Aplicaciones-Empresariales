from django import forms
from .models import Dueno, Raza, Veterinario, Mascota, Consulta


class DuenoForm(forms.ModelForm):
    class Meta:
        model = Dueno
        fields = '__all__'


class RazaForm(forms.ModelForm):
    class Meta:
        model = Raza
        fields = '__all__'


class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = '__all__'


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }