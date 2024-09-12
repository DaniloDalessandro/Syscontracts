from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from .models import LinhaOrcamentaria,Contrato,Prestacao,Remanejamento,Aditivo
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .forms import LinhaOrcamentariaForm,ContratoForm,PrestacaoForm,RemanejamentoForm,AditivoForm
from django.db.models import Sum
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

class LinhaOrcamentariaCreateView(CreateView):
    model = LinhaOrcamentaria
    form_class = LinhaOrcamentariaForm
    template_name = 'linhas/linhaorcamentaria_form.html'
    success_url = reverse_lazy('linha_orcamentaria_list')

class LinhaOrcamentariaUpdateView(UpdateView):
    model = LinhaOrcamentaria
    form_class = LinhaOrcamentariaForm
    template_name = 'linhas/linhaorcamentaria_form.html'
    success_url = reverse_lazy('linha_orcamentaria_list')

class LinhaOrcamentariaDeleteView(DeleteView):
    model = LinhaOrcamentaria
    template_name = 'linhas/linhaorcamentaria_confirm_delete.html'
    success_url = reverse_lazy('linha_orcamentaria_list')

#======================================================================================================================

class ContratoListView(ListView):
    model = Contrato
    template_name = 'contratos/contrato_list.html'
    context_object_name = 'contratos'
    paginate_by = 5

class ContratoCreateView(CreateView):
    model = Contrato
    form_class = ContratoForm
    template_name = 'contratos/contrato_form.html'
    success_url = reverse_lazy('contrato_list')
    
class ContratoUpdateView(UpdateView):
    model = Contrato
    form_class = ContratoForm
    template_name = 'contratos/contrato_form.html'
    success_url = reverse_lazy('contrato_list')

class ContratoDeleteView(DeleteView):
    model = Contrato
    template_name = 'contratos/contrato_confirm_delete.html'
    success_url = reverse_lazy('contrato_list')

class ContratoDetailView(DetailView):
    model = Contrato
    template_name = 'contratos/contrato_detail.html'
    context_object_name = 'contrato'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Filtra as prestações relacionadas ao contrato
        prestacoes = Prestacao.objects.filter(contrato=self.object)
        
        # Calcula o total pago até o momento
        total_pago = prestacoes.aggregate(total=Sum('valor_parcela'))['total'] or 0
        
        # Calcula o valor restante
        valor_restante = self.object.valor_contrato - total_pago
        
        # Adiciona ao contexto
        context['prestações'] = prestacoes
        context['total_pago'] = total_pago
        context['valor_restante'] = valor_restante
        
        return context

#============================================================================================================================

def adicionar_prestacao(request, contrato_id):
    contrato = get_object_or_404(Contrato, pk=contrato_id)
    
    if request.method == 'POST':
        form = PrestacaoForm(request.POST)
        if form.is_valid():
            prestacao = form.save(commit=False)
            prestacao.contrato = contrato  # Relaciona a prestação com o contrato
            prestacao.save()  # O número será automaticamente atribuído no método save()
            return redirect('contrato_detail', pk=contrato.pk)
    else:
        form = PrestacaoForm()

    return render(request, 'contratos/adicionar_prestacao.html', {'form': form, 'contrato': contrato})

class PrestacaoUpdateView(UpdateView):
    model = Prestacao
    form_class = PrestacaoForm
    template_name = 'contratos/editar_prestacao.html'
    
    def get_success_url(self):
        # Aqui garantimos que o redirecionamento use o contrato associado à prestação
        return reverse_lazy('contrato_detail', kwargs={'pk': self.object.contrato.pk})

from django.urls import reverse_lazy

class PrestacaoDeleteView(DeleteView):
    model = Prestacao
    template_name = 'contratos/deletar_prestacao.html'
    
    def get_success_url(self):
        # Redirecionar para os detalhes do contrato após deletar a prestação
        return reverse_lazy('contrato_detail', kwargs={'pk': self.object.contrato.pk})

#========================================================================================================================================================

class RemanejamentoListView(ListView):
    model = Remanejamento
    template_name = 'remanejamentos/remanejamento_list.html'
    context_object_name = 'remanejamentos'
    paginate_by = 5

class RemanejamentoDetailView(DetailView):
    model = Remanejamento
    template_name = 'remanejamentos/remanejamento_detail.html'
    context_object_name = 'remanejamento'

class RemanejamentoCreateView(CreateView):
    model = Remanejamento
    form_class = RemanejamentoForm
    template_name = 'remanejamentos/remanejamento_form.html'
    success_url = reverse_lazy('remanejamento_list')

    def form_valid(self, form):
        remanejamento = form.save(commit=False)
        remanejamento.clean()  # Validação antes de salvar
        return super().form_valid(form)

class RemanejamentoUpdateView(UpdateView):
    model = Remanejamento
    form_class = RemanejamentoForm
    template_name = 'remanejamentos/remanejamento_form.html'
    success_url = reverse_lazy('remanejamento_list')

    def form_valid(self, form):
        remanejamento = form.save(commit=False)
        remanejamento.clean()  # Validação antes de salvar
        return super().form_valid(form)

class RemanejamentoDeleteView(DeleteView):
    model = Remanejamento
    template_name = 'remanejamentos/remanejamento_confirm_delete.html'
    success_url = reverse_lazy('remanejamento_list')

#========================================================================================================================================================

class AditivoListView(ListView):
    model = Aditivo
    template_name = 'aditivos/aditivo_list.html'
    context_object_name = 'aditivos'
    paginate_by = 5

class AditivoDetailView(DetailView):
    model = Aditivo
    template_name = 'aditivos/aditivo_detail.html'
    context_object_name = 'aditivo'

class AditivoCreateView(CreateView):
    model = Aditivo
    form_class = AditivoForm
    template_name = 'aditivos/aditivo_form.html'
    success_url = reverse_lazy('aditivo_list')

class AditivoUpdateView(UpdateView):
    model = Aditivo
    form_class = AditivoForm
    template_name = 'aditivos/aditivo_form.html'
    success_url = reverse_lazy('aditivo_list')

class AditivoDeleteView(DeleteView):
    model = Aditivo
    template_name = 'aditivos/aditivo_confirm_delete.html'
    success_url = reverse_lazy('aditivo_list')