from django import forms
from .models import LinhaOrcamentaria

# =========================================================================================================================

class LinhaOrcamentariaForm(forms.ModelForm):
    class Meta:
        model = LinhaOrcamentaria
        fields = [
            'classe',
            'custo_despesa',
            'centro_custo_gestor',
            'centro_custo_solicitante',
            'descricao_resumida',
            'objeto',
            'classificacao_orcamento',
            'possivel_fiscal',
            'ano_orcamento',
            'tipo_contrato',
            'status_linha_orcamentaria',
            'tipo_provavel_contratacao',
            'valor_orcado',
            'status_elaboracao_tr',
            'necessidade_contratacao',
            'status_processo',
            'status_contratacao',
            'obs_contrato',
        ]
        widgets = {
            'classe': forms.Select(attrs={'class': 'form-control'}),
            'custo_despesa': forms.Select(attrs={'class': 'form-control'}),
            'centro_custo_gestor': forms.Select(attrs={'class': 'form-control'}),
            'centro_custo_solicitante': forms.Select(attrs={'class': 'form-control'}),
            'descricao_resumida': forms.TextInput(attrs={'class': 'form-control'}),
            'objeto': forms.TextInput(attrs={'class': 'form-control'}),
            'classificacao_orcamento': forms.Select(attrs={'class': 'form-control'}),
            'possivel_fiscal': forms.Select(attrs={'class': 'form-control'}),
            'ano_orcamento': forms.Select(attrs={'class': 'form-control'}),
            'tipo_contrato': forms.Select(attrs={'class': 'form-control'}),
            'status_linha_orcamentaria': forms.Select(attrs={'class': 'form-control'}),
            'tipo_provavel_contratacao': forms.Select(attrs={'class': 'form-control'}),
            'valor_orcado': forms.NumberInput(attrs={'class': 'form-control'}),
            'status_elaboracao_tr': forms.Select(attrs={'class': 'form-control'}),
            'necessidade_contratacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status_processo': forms.Select(attrs={'class': 'form-control'}),
            'status_contratacao': forms.Select(attrs={'class': 'form-control'}),
            'obs_contrato': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'classe': 'Tipo de linha',
            'custo_despesa': 'CUSTO/DESPESA',
            'centro_custo_gestor': 'Centro de Custo Gestor',
            'centro_custo_solicitante': 'Centro de Custo Solicitante',
            'descricao_resumida': 'Finalidade',
            'objeto': 'Objeto',
            'classificacao_orcamento': 'Classificação Orçamentária',
            'possivel_fiscal': 'Fiscal',
            'ano_orcamento': 'Ano do Orçamento',
            'tipo_contrato': 'Tipo de Contrato',
            'status_linha_orcamentaria': 'Status da Linha Orçamentária',
            'tipo_provavel_contratacao': 'Tipo de Provável Contratação',
            'valor_orcado': 'Valor Orçado',
            'status_elaboracao_tr': 'Status da Elaboração do TR',
            'necessidade_contratacao': 'Necessidade de Contratação',
            'status_processo': 'Status do Processo',
            'status_contratacao': 'Status da Contratação',
            'obs_contrato': 'Observações do Contrato',
        }