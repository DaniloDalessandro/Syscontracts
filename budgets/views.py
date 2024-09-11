from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Orcamento,OrcamentoExterno
from django.views.generic import ListView,DeleteView,DetailView,UpdateView,CreateView
from .forms import OrcamentoExternoForm,OrcamentoForm

class OrcamentoListView(ListView):
    model = Orcamento
    template_name = 'orcamento_list.html'
    context_object_name = 'orcamentos'
    paginate_by = 5

class OrcamentoDetailView(DetailView):
    model = Orcamento
    template_name = 'orcamento_detail.html'
    context_object_name = 'orcamento'

class OrcamentoCreateView(CreateView):
    model = Orcamento
    form_class = OrcamentoForm
    template_name = 'orcamento_form.html'
    success_url = reverse_lazy('orcamento_list')

class OrcamentoUpdateView(UpdateView):
    model = Orcamento
    form_class = OrcamentoForm
    template_name = 'orcamento_form.html'
    success_url = reverse_lazy('orcamento_list')

class OrcamentoDeleteView(DeleteView):
    model = Orcamento
    template_name = 'orcamento_confirm_delete.html'
    success_url = reverse_lazy('orcamento_list')

#======================================================================================================================

class OrcamentoExternoListView(ListView):
    model = OrcamentoExterno
    template_name = 'orcamentoexterno_list.html'
    context_object_name = 'orcamentos_externos'
    paginate_by = 5

class OrcamentoExternoDetailView(DetailView):
    model = OrcamentoExterno
    template_name = 'orcamentoexterno_detail.html'
    context_object_name = 'orcamento_externo'

class OrcamentoExternoCreateView(CreateView):
    model = OrcamentoExterno
    form_class = OrcamentoExternoForm
    template_name = 'orcamentoexterno_form.html'
    success_url = reverse_lazy('orcamentoexterno_list')

    def form_valid(self, form):
        orcamento_externo = form.save(commit=False)
        # Salva a instância do orçamento principal antes de associar o orçamento externo
        orcamento_externo.ano.save()
        orcamento_externo.save()
        return redirect(self.success_url)

class OrcamentoExternoUpdateView(UpdateView):
    model = OrcamentoExterno
    form_class = OrcamentoExternoForm
    template_name = 'orcamentoexterno_form.html'
    success_url = reverse_lazy('orcamentoexterno_list')

    def form_valid(self, form):
        orcamento_externo = form.save(commit=False)
        orcamento_externo.ano.save()
        orcamento_externo.save()
        return redirect(self.success_url)

class OrcamentoExternoDeleteView(DeleteView):
    model = OrcamentoExterno
    template_name = 'orcamentoexterno_confirm_delete.html'
    success_url = reverse_lazy('orcamentoexterno_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)
    
