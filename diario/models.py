from django.db import models

# Create your models here.
class Pessoa(models.Model):
  nome  = models.CharField(max_length=100)
  foto = models.ImageField(upload_to='foto')

  def __str__(self):
    return self.nome
  

class Diario(models.Model):
  titulo = models.CharField(max_length=100)
  tags = models.TextField()
  texto = models.TextField()
  pessoa = models.ManyToManyField(Pessoa)
  create_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.titulo