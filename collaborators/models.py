from django.db import models
from sectors.models import Direcao,Gerencia,Coordenacao

class Colaborador(models.Model):    
    nome_completo = models.CharField(max_length=100, null=True)
    mat = models.IntegerField(null=True, blank=True,verbose_name='Matrícula',unique=True)     
    direcao = models.ForeignKey(Direcao, on_delete=models.CASCADE,null=True)
    gerencia = models.ForeignKey(Gerencia, on_delete=models.SET_NULL,null=True)
    coordenacao = models.ForeignKey(Coordenacao, on_delete=models.SET_NULL,null=True)
    ramal = models.CharField(max_length=4,null=True, blank=True)
    email = models.EmailField(max_length=50,null=True, blank=True)

    def __str__(self):
        return self.nome_completo or "Colaborador sem Nome"
    
    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'