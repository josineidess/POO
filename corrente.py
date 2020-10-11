from conta import Conta

class Corrente(Conta):
  '''Subclasse Corrente que herda a classe Conta'''

  def __init__(self,nome,cpf,data_nascimento,agencia,numero,senha):
    '''Passando os valores dos parâmetros para os atributos
       herdados da classe mãe Conta'''
    super().__init__(nome,cpf,data_nascimento,agencia,numero,senha,10)