#nesse arquivo criamos nossas classes, nossos models
from django.db import models

# Create your models here.

#classe da base do projeto
class Base(models.Model):
    criacao = models.DateField(auto_now_add=True) #campo de data e hora que vai ser adicionado automaticamente
    atualizacao = models.DateField(auto_now=True) #campo para pegar data e hora de atualização
    ativo = models.BooleanField(default=True) 
    
    class Meta:
        abstract = True
        

class Curso(Base):
    titulo = models.CharField(max_length=255) #titulo do curso, vai ter um limite de tamanho de nome ate 255 caracteres
    url = models.URLField(unique=True) #vai ser um curso online, que tem uma url e essa url tem que ser unica, se não da erro. Cada curso vai ter uma url especifica
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        
    ##função construtora que vai retornar o titulo do curso
    def __str__(self):
        return self.titulo
    

class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)
    
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        unique_together= ['email', 'curso']
        
        def __str__(self):
            return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'
    