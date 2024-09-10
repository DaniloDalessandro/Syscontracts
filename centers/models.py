from django.db import models


# ============================================================================================================

class CentroDeCustoGestor(models.Model):
    nome = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.nome
    
# ============================================================================================================

class CentroDeCustoSolicitante(models.Model):
    centro_gestor = models.ForeignKey(CentroDeCustoGestor, on_delete=models.CASCADE, related_name='solicitantes')
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        unique_together = ('centro_gestor', 'nome')