from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('setores/',include('sectors.urls')),
    path('centros/',include('centers.urls')),
    path('colaborador/',include('collaborators.urls')),
    path('orcamentos/',include('budgets.urls')),
    path('contratos/',include('contracts.urls')),
    path('auxilios/',include('aid.urls')),
    path('',include('dashboard.urls')),
]
