from django.db import models

class Direcao(models.Model):
    nome = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Direção'
        verbose_name_plural = 'Direções'
        
# =====================================================================================================================

class Gerencia(models.Model):
    nome = models.CharField(max_length=100,unique=True)
    direcao = models.ForeignKey(Direcao, on_delete=models.CASCADE, related_name='gerencias')

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Gerência'
        verbose_name_plural = 'Gerências'
        unique_together = ('direcao','nome')

# =====================================================================================================================

class Coordenacao(models.Model):
    nome = models.CharField(max_length=100,unique=True)
    gerencia = models.ForeignKey(Gerencia, on_delete=models.CASCADE, related_name='coordenacoes')

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Coordenação'
        verbose_name_plural = 'Coordenações'
        unique_together = ('gerencia','nome')