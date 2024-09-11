from django.urls import path
from .views import AuxilioColaboradorListView,AuxilioColaboradorDetailView,AuxilioColaboradorCreateView,AuxilioColaboradorUpdateView,AuxilioColaboradorDeleteView

urlpatterns = [
    path('listar_auxilios/', AuxilioColaboradorListView.as_view(), name='auxilio_colaborador_list'),
    path('<int:pk>/', AuxilioColaboradorDetailView.as_view(), name='auxilio_colaborador_detail'),
    path('create/', AuxilioColaboradorCreateView.as_view(), name='auxilio_colaborador_create'),
    path('<int:pk>/update/', AuxilioColaboradorUpdateView.as_view(), name='auxilio_colaborador_update'),
    path('<int:pk>/delete/', AuxilioColaboradorDeleteView.as_view(), name='auxilio_colaborador_delete'),
]
