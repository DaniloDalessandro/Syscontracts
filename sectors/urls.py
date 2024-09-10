from django.urls import path
from .views import GerenciaListView,GerenciaCreateView,GerenciaUpdateView,GerenciaDeleteView
from .views import DirecaoCreateView,DirecaoDeleteView,DirecaoListView,DirecaoUpdateView
from .views import CoordenacaoCreateView,CoordenacaoDeleteView,CoordenacaoListView,CoordenacaoUpdateView

urlpatterns = [
    path('listardirecoes/', DirecaoListView.as_view(), name='direcao_list'),
    path('novadirecao/', DirecaoCreateView.as_view(), name='direcao_create'),
    path('<int:pk>/editardirecao/', DirecaoUpdateView.as_view(), name='direcao_update'),
    path('<int:pk>/deletardirecao/', DirecaoDeleteView.as_view(), name='direcao_delete'),
    # ==============================================================================================
    path('listargerencias/', GerenciaListView.as_view(), name='gerencia_list'),
    path('novagerencia/', GerenciaCreateView.as_view(), name='gerencia_create'),
    path('<int:pk>/editargerencia/', GerenciaUpdateView.as_view(), name='gerencia_update'),
    path('<int:pk>/deletargerencia/', GerenciaDeleteView.as_view(), name='gerencia_delete'),
    # ==============================================================================================
    path('listarcoordenacoes/', CoordenacaoListView.as_view(), name='coordenacao_list'),
    path('novacoordenacao/', CoordenacaoCreateView.as_view(), name='coordenacao_create'),
    path('<int:pk>/editarcoordenacao/', CoordenacaoUpdateView.as_view(), name='coordenacao_update'),
    path('<int:pk>/deletarcoordenacao/', CoordenacaoDeleteView.as_view(), name='coordenacao_delete'),
]