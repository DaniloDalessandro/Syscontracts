from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from .models import CentroDeCustoGestor,CentroDeCustoSolicitante
from .forms import CentroDeCustoGestorForm,CentroDeCustoSolicitanteForm

#======================================================================================================================

class CentroDeCustoGestorListView(ListView):
    model = CentroDeCustoGestor
    template_name = 'centrodecustogestor_list.html'
    context_object_name = 'centros'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return CentroDeCustoGestor.objects.filter(nome__icontains=query)
        return CentroDeCustoGestor.objects.all()
    
class CentroDeCustoGestorCreateView(CreateView):
    model = CentroDeCustoGestor
    form_class = CentroDeCustoGestorForm
    template_name = 'centrodecustogestor_form.html'
    success_url = reverse_lazy('centrodecustogestor_list')

class CentroDeCustoGestorUpdateView(UpdateView):
    model = CentroDeCustoGestor
    form_class = CentroDeCustoGestorForm
    template_name = 'centrodecustogestor_form.html'
    success_url = reverse_lazy('centrodecustogestor_list')

class CentroDeCustoGestorDeleteView(DeleteView):
    model = CentroDeCustoGestor
    template_name = 'centrodecustogestor_confirm_delete.html'
    success_url = reverse_lazy('centrodecustogestor_list')

#======================================================================================================================

class CentroDeCustoSolicitanteListView(ListView):
    model = CentroDeCustoSolicitante
    template_name = 'centrodecustosolicitante_list.html'
    context_object_name = 'solicitantes'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return CentroDeCustoSolicitante.objects.filter(nome__icontains=query)
        return CentroDeCustoSolicitante.objects.all()

class CentroDeCustoSolicitanteCreateView(CreateView):
    model = CentroDeCustoSolicitante
    form_class = CentroDeCustoSolicitanteForm
    template_name = 'centrodecustosolicitante_form.html'
    success_url = reverse_lazy('centrodecustosolicitante_list')

class CentroDeCustoSolicitanteUpdateView(UpdateView):
    model = CentroDeCustoSolicitante
    form_class = CentroDeCustoSolicitanteForm
    template_name = 'centrodecustosolicitante_form.html'
    success_url = reverse_lazy('centrodecustosolicitante_list')

class CentroDeCustoSolicitanteDeleteView(DeleteView):
    model = CentroDeCustoSolicitante
    template_name = 'centrodeustosolicitante_confirm_delete.html'
    success_url = reverse_lazy('centrodecustosolicitante_list')
