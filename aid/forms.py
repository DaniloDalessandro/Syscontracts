from django import forms
from .models import AuxilioColaborador

class AuxilioColaboradorForm(forms.ModelForm):
    class Meta:
        model = AuxilioColaborador
        fields = [
            'beneficiado', 'linha', 'tipo', 'beneficio',
            'valor_parcela', 'qtd_parcelas', 'obs', 'mes_inicio', 'previsao_inicio'
        ]
        widgets = {
            'beneficiado': forms.Select(attrs={'class': 'form-control'}),  # Campo de seleção para o colaborador
            'linha': forms.Select(attrs={'class': 'form-control'}),  # Campo de seleção para a linha orçamentária
            'tipo': forms.Select(attrs={'class': 'form-control'}),  # Campo de seleção para o tipo de auxílio
            'beneficio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe o benefício'}),  # Campo de texto para o benefício
            'valor_parcela': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor da parcela'}),  # Campo numérico para valor por parcela
            'qtd_parcelas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade de parcelas'}),  # Campo numérico para quantidade de parcelas
            'obs': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observações (opcional)'}),  # Campo de texto para observações
            'mes_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # Campo de data com seletor de calendário
            'previsao_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # Campo de data com seletor de calendário
        }
