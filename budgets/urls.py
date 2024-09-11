from django.urls import path
from .views import OrcamentoListView,OrcamentoDetailView,OrcamentoCreateView,OrcamentoUpdateView,OrcamentoDeleteView
from .views import OrcamentoExternoCreateView,OrcamentoExternoDeleteView,OrcamentoExternoDetailView,OrcamentoExternoListView,OrcamentoExternoUpdateView

urlpatterns = [
    path('orcamentos_internos/', OrcamentoListView.as_view(), name='orcamento_list'),
    path('orcamentos_internos/<int:pk>/', OrcamentoDetailView.as_view(), name='orcamento_detail'),
    path('orcamentos_internos/create/', OrcamentoCreateView.as_view(), name='orcamento_create'),
    path('orcamentos_internos/<int:pk>/update/', OrcamentoUpdateView.as_view(), name='orcamento_update'),
    path('orcamentos_internos/<int:pk>/delete/', OrcamentoDeleteView.as_view(), name='orcamento_delete'),

    # ==============================================================================================
    path('orcamentos_externos/', OrcamentoExternoListView.as_view(), name='orcamento_externo_list'),
    path('orcamentos_externos/<int:pk>/', OrcamentoExternoDetailView.as_view(), name='orcamento_externo_detail'),
    path('orcamentos_externos/create/', OrcamentoExternoCreateView.as_view(), name='orcamento_externo_create'),
    path('orcamentos_externos/<int:pk>/update/', OrcamentoExternoUpdateView.as_view(), name='orcamento_externo_update'),
    path('orcamentos_externos/<int:pk>/delete/', OrcamentoExternoDeleteView.as_view(), name='orcamento_externo_delete'),

]