from django.urls import path
from .views import LinhaOrcamentariaCreateView,LinhaOrcamentariaDeleteView,LinhaOrcamentariaDetailView,LinhaOrcamentariaListView,LinhaOrcamentariaUpdateView

urlpatterns = [
    path('linhaorcamentaria/', LinhaOrcamentariaListView.as_view(), name='linha_orcamentaria_list'),
    path('linhaorcamentaria/nova/', LinhaOrcamentariaCreateView.as_view(), name='linha_orcamentaria_create'),
    path('linhaorcamentaria/<int:pk>/', LinhaOrcamentariaDetailView.as_view(), name='linha_orcamentaria_detail'),
    path('linhaorcamentaria/<int:pk>/editar/', LinhaOrcamentariaUpdateView.as_view(), name='linha_orcamentaria_update'),
    path('linhaorcamentaria/<int:pk>/deletar/', LinhaOrcamentariaDeleteView.as_view(), name='linha_orcamentaria_delete'),

]