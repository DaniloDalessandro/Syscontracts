from django.urls import path
from .views import ColaboradorCreateView,ColaboradorListView,ColaboradorDeleteView,ColaboradorUpdateView,ColaboradorDetailView

urlpatterns = [
    path('colaboradores/', ColaboradorListView.as_view(), name='colaborador_list'),
    path('colaboradores/novo/', ColaboradorCreateView.as_view(), name='colaborador_create'),
    path('colaboradores/<int:pk>/editar/', ColaboradorUpdateView.as_view(), name='colaborador_update'),
    path('colaboradores/<int:pk>/deletar/', ColaboradorDeleteView.as_view(), name='colaborador_delete'),
    path('colaboradores/<int:pk>/', ColaboradorDetailView.as_view(), name='colaborador_detail'),
]