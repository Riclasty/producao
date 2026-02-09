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
    gestante = models.CharField(max_length=5, null= True)
    pccu =   models.CharField(max_length= 5, null=True)
    data_preventivo =  models.CharField(max_length=100, null=True)
    


    familia = models.ForeignKey(
        Familia,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='pessoas'
    )

    def __str__(self):
        return self.nome