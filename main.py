#Arquivo para testes#

from corrente import Corrente
from poupanca import Poupanca   
from datetime import date
import os
import random

###################
#Criação de contas#
###################

conta1 = Poupanca("Josineide",5678901346,date(2000,2,14),2007,65432,7890)
conta2 = Corrente("Josineide",4566787356,date(2000,2,14),2008,45674,9056)

#Dicionário que guarda as contas que podem ser pesquisadas pelo cpf
contas = {5678901346:conta1,4566787356:conta2}

####################
#Simulação de caixa#
####################


def inicio():
  print("-"*40)
  print("Banco Herascard".center(40))
  print("-"*40)
  print("Seja bem vindo, escolha uma das opções abaixo:\n")
  print("1 - Criar conta poupança\n2 - Criar conta corrente\n3 - Acessar conta\n4 - Finalizar")
  print("-"*40)
  resposta = int(input(": "))
  return resposta


def criar_conta(resposta):
  os.system('clear') or None
  print("-"*40)
  print("Banco Herascard".center(40))
  print("-"*40)
  print("#### Crie sua conta ####".center(40))
  nome = input("\nNome: ")
  cpf = input("CPF: ")
  data = input("Data de nascimento: ")
  senha = input("Digite uma senha: ")
  agencia = random.randint(2010,2100)
  numero_conta = random.randint(1000,9999)
  
  if(resposta == 1):
    conta = Poupanca(nome,cpf,data,agencia,numero_conta,senha)
    contas[conta.cpf]= conta
  else:
    conta = Corrente(nome,cpf,data,agencia,numero_conta,senha)
    contas[conta.cpf] = conta


def acessar_conta():
  cpf = input("Digite seu CPF: ")
  os.system('clear') or None
  print("-"*40)
  print("Banco Herascard".center(40))
  print("-"*40)
  print("### Conta ###".center(40))
  print(f'\nNome: {contas[cpf].nome}\nConta: {contas[cpf].agencia} {contas[cpf].numero}')
  resposta = int(input("1 - Consultar saldo\n2 - Saque\n3 - Deposito\n4 - Alterar senha\n5 - Voltar ao menu\n:"))
      
  while(resposta != 5):
    if(resposta == 1):
      print(f'R$ {contas[cpf].saldo}')
      resposta = int(input("1 - Consultar saldo\n2 - Saque\n3 - Deposito\n4 - Alterar senha\n5 - Voltar ao menu\n:"))
    elif(resposta == 2):
      valor = float(input("Valor para saque: "))
      print(contas[cpf].saque(valor))
      resposta = int(input("1 - Consultar saldo\n2 - Saque\n3 - Deposito\n4 - Alterar senha\n5 - Voltar ao menu\n:"))
    elif(resposta == 3):
      valor = float(input("Valor para deposito: "))
      print(contas[cpf].deposito(valor))
      resposta = int(input("1 - Consultar saldo\n2 - Saque\n3 - Deposito\n4 - Alterar senha\n5 - Voltar ao menu\n:"))
    elif(resposta == 4):
      nova_senha = input("Nova senha: ")
      if(len(nova_senha) == 4):
        contas[cpf].senha = nova_senha
        print("Senha alterada.")
        resposta = int(input("1 - Consultar saldo\n2 - Saque\n3 - Deposito\n4 - Alterar senha\n5 - Voltar ao menu\n:"))
      else:
        print("insira uma senha de 4 digitos")
        resposta = int(input("1 - Consultar saldo\n2 - Saque\n3 - Deposito\n4 - Alterar senha\n5 - Voltar ao menu\n:"))
    elif(resposta == 5):
        os.system('clear') or None
        inicio()
        

def main():
  res = inicio()
  while(res != 4):
    if(res == 1):
      criar_conta(res)
      res = inicio()
    elif(res == 2):
      criar_conta(res)
      res = inicio()
    elif(res == 3):
      acessar_conta()
      res = inicio()
  if(res == 4):
    print("Obrigado por utilizar nosso banco!")

if(__name__ == '__main__'):
  main()  




