from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Coordenacao,Gerencia,Direcao
from .forms import CoordenacaoForm,GerenciaForm,DirecaoForm
from django.views.generic import ListView,CreateView, UpdateView, DeleteView

# ===============================================================================================================

class DirecaoListView(ListView):
    model = Direcao
    template_name = 'direcao_list.html'
    context_object_name = 'direcoes'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Direcao.objects.filter(nome__icontains=query)
        return Direcao.objects.all()
    
    paginate_by = 5

class DirecaoCreateView(CreateView):
    model = Direcao
    form_class = DirecaoForm
    template_name = 'direcao_form.html'
    success_url = reverse_lazy('direcao_list')

class DirecaoUpdateView(UpdateView):
    model = Direcao
    form_class = DirecaoForm
    template_name = 'direcao_form.html'
    success_url = reverse_lazy('direcao_list')

class DirecaoDeleteView(DeleteView):
    model = Direcao
    template_name = 'direcao_confirm_delete.html'
    success_url = reverse_lazy('direcao_list')

# ===============================================================================================================

class GerenciaListView(ListView):
    model = Gerencia
    template_name = 'gerencia_list.html'
    context_object_name = 'gerencias'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Gerencia.objects.filter(nome__icontains=query)
        return Gerencia.objects.all()

class GerenciaCreateView(CreateView):
    model = Gerencia
    form_class = GerenciaForm
    template_name = 'gerencia_form.html'
    success_url = reverse_lazy('gerencia_list')

class GerenciaUpdateView(UpdateView):
    model = Gerencia
    form_class = GerenciaForm
    template_name = 'gerencia_form.html'
    success_url = reverse_lazy('gerencia_list')

class GerenciaDeleteView(DeleteView):
    model = Gerencia
    template_name = 'gerencia_confirm_delete.html'
    success_url = reverse_lazy('gerencia_list')

#======================================================================================================================

class CoordenacaoListView(ListView):
    model = Coordenacao
    template_name = 'coordenacao_list.html'
    context_object_name = 'coordenacoes'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Coordenacao.objects.filter(nome__icontains=query)
        return Coordenacao.objects.all()

class CoordenacaoCreateView(CreateView):
    model = Coordenacao
    form_class = CoordenacaoForm
    template_name = 'coordenacao_form.html'
    success_url = reverse_lazy('coordenacao_list')

class CoordenacaoUpdateView(UpdateView):
    model = Coordenacao
    form_class = CoordenacaoForm
    template_name = 'coordenacao_form.html'
    success_url = reverse_lazy('coordenacao_list')

class CoordenacaoDeleteView(DeleteView):
    model = Coordenacao
    template_name = 'coordenacao_confirm_delete.html'
    success_url = reverse_lazy('coordenacao_list')