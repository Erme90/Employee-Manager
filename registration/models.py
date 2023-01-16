from uuid import uuid1, uuid4
from django.contrib.auth.models import User
from django.db import models

#O model, é onde se cria o banco de dados



class Register_Model(models.Model):
    SEXO_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('N', 'Nenhuma das opções')
    )
    SETOR_CHOICES = (
        ('DP', 'Departamento Pessoal'),
        ('TI', 'Departamento de TI'),
        ('RH', 'Recursos Humanos'),
        ('AMOX', 'Almoxarifado')
    )

    FUNCAO_CHOICES = (
        ('DEV', 'Developer JR'),
        ('DEV', 'Developer PLENO'),
        ('DEV', 'Developer SENIOR'),
        ('TEC_LEAD', 'Tech Lead'),
        ('Analista', 'Analista de RH'),
        ('Gerente', 'Gerente')
    )
    

    nome = models.CharField(max_length=50, null=False)
    nascimento = models.DateField(null=False, unique=True)
    CPF = models.CharField(max_length=11, unique=True, null=False)
    sexo = models.CharField(max_length=15, choices=SEXO_CHOICES, null=True)
    endereco = models.CharField(max_length=50)
    data_admissão = models.DateField(unique=True)
    contrato = models.CharField(max_length=4, null=False, unique=True)
    função = models.CharField(max_length=15, choices = FUNCAO_CHOICES, null=False)
    salario = models.DecimalField(max_digits=5, decimal_places=3)
    setor = models.CharField(max_length=12, choices=SETOR_CHOICES, null=False)
   
    def __str__(self):
        return self.nome
