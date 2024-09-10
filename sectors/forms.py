from django import forms
from .models import Direcao, Gerencia,Coordenacao


# =========================================================================================================================

class DirecaoForm(forms.ModelForm):
    class Meta:
        model = Direcao
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
        }
        labels = {
            'nome': 'Nome',
        }

# =========================================================================================================================

class GerenciaForm(forms.ModelForm):
    class Meta:
        model = Gerencia
        fields = ['direcao', 'nome']
        widgets = {
            'direcao': forms.Select(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
        }
        labels = {
            'direcao': 'Direção',
            'nome': 'Nome',
        }

# =========================================================================================================================

class CoordenacaoForm(forms.ModelForm):
    class Meta:
        model = Coordenacao
        fields = ['gerencia', 'nome']
        widgets = {
            'gerencia': forms.Select(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
        }
        labels = {
            'gerencia': 'Gerência',
            'nome': 'Nome',
        }
