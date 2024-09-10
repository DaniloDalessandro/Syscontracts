from django import forms
from .models import CentroDeCustoGestor,CentroDeCustoSolicitante

# =========================================================================================================================

class CentroDeCustoGestorForm(forms.ModelForm):
    class Meta:
        model = CentroDeCustoGestor
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
        }
        labels = {
            'nome': 'Nome',
        }

# =========================================================================================================================

class CentroDeCustoSolicitanteForm(forms.ModelForm):
    class Meta:
        model = CentroDeCustoSolicitante
        fields = ['centro_gestor', 'nome']
        widgets = {
            'centro_gestor': forms.Select(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
        }
        labels = {
            'centro_gestor': 'Centro Gestor',
            'nome': 'Nome',
        }