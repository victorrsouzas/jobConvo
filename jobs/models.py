from django.contrib.auth.models import User
from django.db import models

class Vaga(models.Model):
    FAIXAS_SALARIAIS = (
        ('A', 'Até 1.000'),
        ('B', 'De 1.000 a 2.000'),
        ('C', 'De 2.000 a 3.000'),
        ('D', 'Acima de 3.000'),
    )

    ESCOLARIDADES = (
        ('EF', 'Ensino Fundamental'),
        ('EM', 'Ensino Médio'),
        ('TG', 'Tecnólogo'),
        ('ES', 'Ensino Superior'),
        ('PS', 'Pós / MBA / Mestrado'),
        ('DR', 'Doutorado'),
    )

    nome = models.CharField(max_length=100)
    faixa_salarial = models.CharField(max_length=1, choices=FAIXAS_SALARIAIS)
    requisitos = models.CharField(max_length=2, choices=ESCOLARIDADES)
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)

class Candidato(models.Model):
    PRETENSAO_SALARIAL = (
        ('A', 'Até 1.000'),
        ('B', 'De 1.000 a 2.000'),
        ('C', 'De 2.000 a 3.000'),
        ('D', 'Acima de 3.000'),
    )

    ESCOLARIDADES = (
        ('EF', 'Ensino Fundamental'),
        ('EM', 'Ensino Médio'),
        ('TG', 'Tecnólogo'),
        ('ES', 'Ensino Superior'),
        ('PS', 'Pós / MBA / Mestrado'),
        ('DR', 'Doutorado'),
    )

    pretensao_salarial = models.CharField(max_length=1, choices=PRETENSAO_SALARIAL)
    experiencia = models.TextField()
    ultima_escolaridade = models.CharField(max_length=2, choices=ESCOLARIDADES)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE, related_name='candidatos')
    

    def calcular_pontuacao(self, vaga):
        pontuacao = 0

        if self.pretensao_salarial == vaga.faixa_salarial:
            pontuacao += 1

        if self.ultima_escolaridade in ['PS', 'DR']:
            pontuacao += 1

        return pontuacao
