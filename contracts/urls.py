from django.urls import path
from .views import LinhaOrcamentariaCreateView,LinhaOrcamentariaDeleteView,LinhaOrcamentariaDetailView,LinhaOrcamentariaListView,LinhaOrcamentariaUpdateView
from .views import ContratoCreateView,ContratoDeleteView,ContratoDetailView,ContratoListView,ContratoUpdateView
from .views import adicionar_prestacao,PrestacaoDeleteView,PrestacaoUpdateView
from .views import RemanejamentoCreateView,RemanejamentoDeleteView,RemanejamentoDetailView,RemanejamentoListView,RemanejamentoUpdateView
from .views import AditivoCreateView,AditivoDeleteView,AditivoDetailView,AditivoListView,AditivoUpdateView

urlpatterns = [
    path('linhaorcamentaria/', LinhaOrcamentariaListView.as_view(), name='linha_orcamentaria_list'),
    path('linhaorcamentaria/nova/', LinhaOrcamentariaCreateView.as_view(), name='linha_orcamentaria_create'),
    path('linhaorcamentaria/<int:pk>/', LinhaOrcamentariaDetailView.as_view(), name='linha_orcamentaria_detail'),
    path('linhaorcamentaria/<int:pk>/editar/', LinhaOrcamentariaUpdateView.as_view(), name='linha_orcamentaria_update'),
    path('linhaorcamentaria/<int:pk>/deletar/', LinhaOrcamentariaDeleteView.as_view(), name='linha_orcamentaria_delete'),
    #=====================================================================================================================
    path('novo_contrato/', ContratoCreateView.as_view(), name='contrato_create'),
    path('list_contrato/', ContratoListView.as_view(), name='contrato_list'),
    path('<int:pk>/editar/', ContratoUpdateView.as_view(), name='contrato_update'),
    path('<int:pk>/deletar/', ContratoDeleteView.as_view(), name='contrato_delete'),       
    path('contrato/<int:pk>/', ContratoDetailView.as_view(), name='contrato_detail'),
    #=====================================================================================================================
    path('contrato/<int:contrato_id>/adicionar-prestacao/', adicionar_prestacao, name='adicionar_prestacao'),
    path('prestacao/<int:pk>/editar/', PrestacaoUpdateView.as_view(), name='editar_prestacao'),
    path('prestacao/<int:pk>/deletar/', PrestacaoDeleteView.as_view(), name='deletar_prestacao'),
    #=====================================================================================================================
    path('remanejamentos/', RemanejamentoListView.as_view(), name='remanejamento_list'),
    path('remanejamentos/<int:pk>/', RemanejamentoDetailView.as_view(), name='remanejamento_detail'),
    path('remanejamentos/novo/', RemanejamentoCreateView.as_view(), name='remanejamento_create'),
    path('remanejamentos/<int:pk>/editar/', RemanejamentoUpdateView.as_view(), name='remanejamento_update'),
    path('remanejamentos/<int:pk>/deletar/', RemanejamentoDeleteView.as_view(), name='remanejamento_delete'),
    #=====================================================================================================================
    path('aditivos/', AditivoListView.as_view(), name='aditivo_list'),
    path('aditivos/<int:pk>/', AditivoDetailView.as_view(), name='aditivo_detail'),
    path('aditivos/novo/', AditivoCreateView.as_view(), name='aditivo_create'),
    path('aditivos/<int:pk>/editar/', AditivoUpdateView.as_view(), name='aditivo_update'),
    path('aditivos/<int:pk>/excluir/', AditivoDeleteView.as_view(), name='aditivo_delete'),

]