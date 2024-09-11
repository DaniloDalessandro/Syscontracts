from django import forms
from .models import Orcamento,OrcamentoExterno

class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['ano', 'centro', 'classe', 'valor']
        widgets = {
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'centro': forms.Select(attrs={'class': 'form-control'}),
            'classe': forms.Select(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'ano': 'Ano',
            'centro': 'Centro de Custo Gestor',
            'classe': 'Classe',
            'valor': 'Valor',
        }

# =========================================================================================================================

class OrcamentoExternoForm(forms.ModelForm):
    class Meta:
        model = OrcamentoExterno
        fields = ['ano', 'centro', 'classe', 'valor', 'tipo_movimentacao']

    def __init__(self, *args, **kwargs):
        super(OrcamentoExternoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})