from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class RegistroConexao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    timestamp_conexao = models.DateTimeField()
    status = models.CharField(max_length=30)
    informacoes_adicionais = models.TextField(blank=True)

    def __str__(self):
        return f"{self.usuario.nome} - {self.timestamp_conexao}"
