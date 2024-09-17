from django import forms
from .models import AuxilioColaborador, LinhaOrcamentaria

class AuxilioColaboradorForm(forms.ModelForm):
    class Meta:
        model = AuxilioColaborador
        fields = [
            'beneficiado', 'linha', 'tipo', 'beneficio',
            'valor_parcela', 'qtd_parcelas', 'obs', 'mes_inicio', 'previsao_inicio'
        ]
        widgets = {
            'beneficiado': forms.Select(attrs={'class': 'form-control'}),
            'linha': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'beneficio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe o benefício'}),
            'valor_parcela': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor da parcela'}),
            'qtd_parcelas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade de parcelas'}),
            'obs': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observações (opcional)'}),
            'mes_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'previsao_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar o campo linha para mostrar apenas linhas com classe CAPEX
        if 'linha' in self.fields:
            self.fields['linha'].queryset = LinhaOrcamentaria.objects.filter(classe='CAPEX')
