from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import AuxilioColaborador
from .forms import AuxilioColaboradorForm
from django.db.models import Sum
from datetime import date

class AuxilioColaboradorListView(ListView):
    model = AuxilioColaborador
    template_name = 'auxiliocolaborador_list.html'
    context_object_name = 'auxilios_colaboradores'
    paginate_by = 5
  
class AuxilioColaboradorDetailView(DetailView):
    model = AuxilioColaborador
    template_name = 'auxiliocolaborador_detail.html'
    context_object_name = 'auxilio_colaborador'

class AuxilioColaboradorCreateView(CreateView):
    model = AuxilioColaborador
    form_class = AuxilioColaboradorForm
    template_name = 'auxiliocolaborador_form.html'
    success_url = reverse_lazy('auxilio_colaborador_list')


class AuxilioColaboradorUpdateView(UpdateView):
    model = AuxilioColaborador
    form_class = AuxilioColaboradorForm
    template_name = 'auxiliocolaborador_form.html'
    success_url = reverse_lazy('auxilio_colaborador_list')

class AuxilioColaboradorDeleteView(DeleteView):
    model = AuxilioColaborador
    template_name = 'auxiliocolaborador_confirm_delete.html'
    success_url = reverse_lazy('auxilio_colaborador_list')
