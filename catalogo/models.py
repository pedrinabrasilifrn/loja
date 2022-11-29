from django.db import models
from django.utils import timezone
import datetime

#Tipo: id, descricao
class Tipo(models.Model):
    descricao = models.CharField("Descrição", max_length=100)
    dt_cad = models.DateTimeField("Data de cadastro") 
    
    class Meta:
        ordering = ['dt_cad']
    
    def __str__(self):
        return self.descricao

    def cadastrado_recentemente(self):
        return self.dt_cad >= timezone.now() - datetime.timedelta(days=1)

UNIDADES_CHOICES = [
        (1, "Kilos"),
        (2, "Litros"),
        (3, "Und"),
        (4, "Metro"),
]
    
#Produto: id, descricao, unidade, preco, estoque, foto
class Produto(models.Model):
    descricao = models.CharField("Descrição", max_length=260, null=False, blank = False)
    unidade = models.IntegerField("Unidade", default=3, choices = UNIDADES_CHOICES)
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    estoque = models.DecimalField(decimal_places=2, max_digits=8)  
    foto = models.ImageField(upload_to='catalogo_img')
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    dt_cad = models.DateTimeField("Data de cadastro") 
    
    class Meta:
        ordering = ['dt_cad']
    
    def __str__(self):
        return self.descricao