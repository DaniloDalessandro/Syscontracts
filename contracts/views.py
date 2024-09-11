from django.shortcuts import render
from django.urls import reverse_lazy
from .models import LinhaOrcamentaria
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .forms import LinhaOrcamentariaForm
#======================================================================================================================

class LinhaOrcamentariaListView(ListView):
    model = LinhaOrcamentaria
    template_name = 'linhas/linhaorcamentaria_list.html'
    context_object_name = 'linhaorcamentarias'
    paginate_by = 5

class LinhaOrcamentariaDetailView(DetailView):
    model = LinhaOrcamentaria
    template_name = 'linhas/linhaorcamentaria_detail.html'
    context_object_name = 'linhaorcamentaria'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        linha = self.object
        context['valor_aprovisionado'] = linha.valor_aprovisionado
        context['valor_remanejado_total'] = linha.valor_remanejado_total
        context['saldo_orcamentario_pos_remanejamento'] = linha.saldo_orcamentario_pos_remanejamento
        context['tempo_para_contratacao'] = linha.tempo_para_contratacao
        return context

class LinhaOrcamentariaCreateView(CreateView):
    model = LinhaOrcamentaria
    form_class = LinhaOrcamentariaForm
    template_name = 'linhas/linhaorcamentaria_form.html'
    success_url = reverse_lazy('linhaorcamentaria_list')

class LinhaOrcamentariaUpdateView(UpdateView):
    model = LinhaOrcamentaria
    form_class = LinhaOrcamentariaForm
    template_name = 'linhas/linhaorcamentaria_form.html'
    success_url = reverse_lazy('linhaorcamentaria_list')

class LinhaOrcamentariaDeleteView(DeleteView):
    model = LinhaOrcamentaria
    template_name = 'linhas/linhaorcamentaria_confirm_delete.html'
    success_url = reverse_lazy('linhaorcamentaria_list')