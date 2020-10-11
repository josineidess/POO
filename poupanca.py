from conta import Conta

class Poupanca(Conta):
  '''Subclasse Poupanca que herda a classe Conta'''

  def __init__(self,nome,cpf,data_nascimento,agencia,numero,senha):
    '''Passando os valores dos parâmetros para os atributos
       herdados da classe mãe Conta'''
    super().__init__(nome,cpf,data_nascimento,agencia,numero,senha)
        
  def saque(self,valor):
    '''Método que sobrescreve o método saque
     da classa mãe para impossibilitar que o saldo seja negativo'''

    if(super().saldo + 2 >= valor): #chamada do método get da classe mãe mais a taxa para checar se está dentro da condição
      super().saque(valor+2) #chamada do método saque da classe mãe para retirada de valores 
      return f'R$ {valor} foi retirado.'
    else:
      return 'Saque indispovível'

  def rende(self):
    '''Método que aumenta em 0.95% o saldo da conta quando chamado'''
    valor = super().saldo
    valor = valor + valor * 0.0095
    super().altera(valor) #método que da classe mãe que altera o valor do saldo
