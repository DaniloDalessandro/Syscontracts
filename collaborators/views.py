from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Colaborador
from .forms import ColaboradorForm
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView

#======================================================================================================================
class ColaboradorListView(ListView):
    model = Colaborador
    template_name = 'colaborador_list.html'
    context_object_name = 'colaboradores'
    paginate_by = 5

class ColaboradorCreateView(CreateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'colaborador_form.html'
    success_url = reverse_lazy('colaborador_list')

class ColaboradorUpdateView(UpdateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'colaborador_form.html'
    success_url = reverse_lazy('colaborador_list')

class ColaboradorDeleteView(DeleteView):
    model = Colaborador
    template_name = 'colaborador_confirm_delete.html'
    success_url = reverse_lazy('colaborador_list')

class ColaboradorDetailView(DetailView):
    model = Colaborador
    template_name = 'colaborador_detail.html'
    context_object_name = 'colaborador'