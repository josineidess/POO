
class Conta:
  '''Classe mãe Conta que contém as informações principais de uma conta genérica.'''

  def __init__(self,nome,cpf,data_nascimento,agencia,numero,senha,ehPoupanca=13):
    '''Número da agencia,nome,cpf,data de nascimento,
       numero da conta,senha e saldo.'''

    self.__agencia = agencia
    self.__nome = nome
    self.__cpf = cpf
    self.__data_nascimento = data_nascimento
    self.__numero = numero
    self.__senha = senha
    self.__saldo = 0
    self.__ehpoupanca = 13

  @property  
  def saldo(self):
    '''get para self.__saldo'''
    return self.__saldo
  
  @property
  def ehpoupanca(self):
    return self.__ehpoupanca

  @property
  def agencia(self):
    '''get para self.__agencia'''
    return self.__agencia

  @property
  def nome(self):
    '''get para self.__nome'''
    return self.__nome

  @property
  def data_nascimento(self):
    '''get para self.__data_nascimento'''
    return self.__data_nascimento
  
  @property
  def cpf(self):
    '''get para self.__cpf'''
    return self.__cpf

  @property
  def numero(self):
    '''get para self.__numero'''
    return self.__numero

  @property
  def senha(self):
    '''get para self.__senha'''
    return self.__senha

  @senha.setter
  def senha(self,nsenha):
    '''setter para self.__senha'''
    self.__senha = nsenha 
  
  def saque(self,valor):
    '''método para saque'''
    self.__saldo -= valor
    return f'R$ {valor} foi retirado.'
  
  def deposito(self,valor):
    '''método para depósito'''
    self.__saldo += valor
    return f'R$ {valor} foi adicionado.'
  
  def altera(self,valor):
    '''método que modifica o saldo,
     para o uso do método rende da classe poupança'''
    self.__saldo = valor

