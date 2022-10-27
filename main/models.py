from django.db import models

class Cliente(models.Model):
  nome = models.CharField(max_length=200, null=False)
  email = models.EmailField()
  endereco = models.CharField(max_length=200, blank=True)

class Categoria(models.Model):
  nome = nome = models.CharField(max_length=200, null=False)

class Filme(models.Model):
  titulo = models.CharField(max_length=200, null=False)
  ano_lancamento = models.DateField()
  valor_locacao = models.FloatField()
  categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Locacao(models.Model):
  data_entrega = models.DateTimeField()
  data_locacao = models.DateTimeField()
  valor = models.FloatField()
  cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
  filme_id = models.ManyToManyField(Filme)



