from django.urls import path
from centers.views import CentroDeCustoGestorCreateView, CentroDeCustoGestorListView,CentroDeCustoGestorDeleteView,CentroDeCustoGestorUpdateView
from .views import CentroDeCustoSolicitanteCreateView,CentroDeCustoSolicitanteDeleteView,CentroDeCustoSolicitanteListView,CentroDeCustoSolicitanteUpdateView

urlpatterns = [

    path('listarcentrogestor/', CentroDeCustoGestorListView.as_view(), name='centro_gestor_list'),
    path('novogestor/', CentroDeCustoGestorCreateView.as_view(), name='centro_gestor_create'),
    path('<int:pk>/editarcentrodecusto/', CentroDeCustoGestorUpdateView.as_view(), name='centro_gestor_update'),
    path('<int:pk>/deletarcentrodecusto/', CentroDeCustoGestorDeleteView.as_view(), name='centro_gestor_delete'),
    # ==========================================================================================================================
    path('listarcentrosolicitante/', CentroDeCustoSolicitanteListView.as_view(), name='centro_solicitante_list'),
    path('novosolicitante/', CentroDeCustoSolicitanteCreateView.as_view(), name='centro_solicitante_create'),
    path('<int:pk>/editarsolicitante/', CentroDeCustoSolicitanteUpdateView.as_view(), name='centro_solicitante_update'),
    path('<int:pk>/deletarsolicitante/', CentroDeCustoSolicitanteDeleteView.as_view(), name='centro_solicitante_delete'),

]