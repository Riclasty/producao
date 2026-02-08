from django.db import models

class Familia(models.Model):
    nome = models.CharField(max_length=50)
    nis = models.CharField(max_length= 15, null= True)
    

    def __str__(self):
        return self.nome

        
class Pessoa(models.Model):
    nome = models.CharField(max_length=100, null=True)
    idade = models.IntegerField()
    data_nascimento = models.DateField(null=True)
    altura = models.DecimalField(null=True,max_digits=3, decimal_places=2 )
    peso = models.DecimalField(null=True, max_digits=4, decimal_places=1)
    vacina = models.BooleanField(default=False)
    gestante = models.BooleanField(default=False)
    
    


    familia = models.ForeignKey(
        Familia,
        on_delete=models.CASCADE,
        related_name='pessoas'
    )

    def __str__(self):
        return self.nome