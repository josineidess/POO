#Arquivo para testes#

from corrente import Corrente
from poupanca import Poupanca   
from datetime import date
import os
import random


###################
#Criação de contas#
###################

conta1 = Poupanca("Josineide","5678901346",date(2000,2,14),2007,65432,7890)
conta2 = Corrente("Josineide","4566787356",date(2000,2,14),2008,45674,9056)

#Dicionário que guarda as contas que podem ser pesquisadas pelo cpf
contas = {conta1.cpf:conta1,conta2.cpf:conta2}

####################
#Simulação de caixa#
####################

#O sistema não está todo com correção de valores

def cabecalho():
  '''Função que ilustra cabeçalho'''
  print("-"*40)
  print("Banco Herascard".center(40))
  print("-"*40)

def limpar():
  return os.system("clear") or None #Comando para limpar tela

def inicio():
  '''Função que exibe menu principal'''

  cabecalho()
  print("Seja bem vindo, escolha uma das opções abaixo:\n")
  print("1 - Criar conta poupança\n2 - Criar conta corrente\n3 - Acessar conta\n4 - Finalizar")
  print("-"*40)
  resposta = int(input(": "))
  return resposta


def criar_conta(resposta):
  '''Função que cria contas poupanças e corrente utilizando
   as subclasses Corrente e Poupanca'''

  #Estilização
  limpar()
  cabecalho()
  print("#### Crie sua conta ####".center(40))

  #Entrada de dados
  '''Entrada de valores correspondentes aos atributos da classe'''
  
  nome = input("\nNome: ")
  cpf = input("CPF: ")
  #condição que checa se existe o mesmo cpf e com o mesmo tipo de conta
  while(cpf in contas and ((resposta == 1 and contas[cpf].ehpoupanca == 13) or resposta == 2 and contas[cpf].ehpoupanca == 10)):
    print("Esse cpf já existe, digite outro")
    cpf = input("CPF: ")
  data = input("Data de nascimento(yyyy,m,d): ")
  senha = int(input("Digite uma senha(4 dígitos): "))
  while(len(str(senha))!= 4):
    senha = int(input("Digite uma senha(4 dígitos): "))

  '''Atribudos gerados automaticamente'''
  agencia = random.randint(2010,2100) #O número da agencia é sorteado por meio da funcao randint
  numero_conta = random.randint(1000,9999) #O número da conta é sorteado da mesma forma
  
  '''Condição para checar tipo de conta'''

  if(resposta == 1):
    conta = Poupanca(nome,cpf,data,agencia,numero_conta,senha)
    contas[conta.cpf]= conta #Adicionando nova conta para o dicionário
  elif(resposta == 2):
    conta = Corrente(nome,cpf,data,agencia,numero_conta,senha)
    contas[conta.cpf] = conta #Adicionando nova conta para o dicionári
  
  '''Encerramento da criação e volta para o menu'''

  print("\nConta criada com sucesso!\n")
  voltar = input("Deseja voltar ao menu?(S,N):")
  voltar = voltar.upper() #método que deixa a letra maíscula
  return voltar #Resposta é enviada de volta para a função menu

def acessar_conta():
  '''Função resposável pelo submenu com as opções de acesso da conta'''
  
  #Estilização

  limpar()
  cabecalho()

  '''Leitura de dados para acesso da conta'''

  cpf = input("\nDigite seu CPF: ")
  senha = int(input("Digite sua senha: "))
  #Vericação de dados
  if(contas[cpf].cpf == cpf and contas[cpf].senha == senha):
    #Estilizaçãp
    limpar()
    cabecalho()
    print("### Conta ###".center(40))

    '''Variável que armazena o tipo da conta(Poupança ou Corrente)'''
   
    tipo = ""
    if(contas[cpf].ehpoupanca == 13):
      tipo = " - Poupança"
    else:
       tipo = " - Corrente"

    '''Visualização de dados'''

    print(f'\nNome: {contas[cpf].nome}\nConta: {contas[cpf].agencia} {contas[cpf].numero}\nTipo: {contas[cpf].ehpoupanca}{tipo}')
    print("-"*40)
    resposta = int(input("1 - Consultar saldo\n2 - Saque\n3 - Deposito\n4 - Alterar senha\n5 - Voltar ao menu\n:"))
  else:
    '''Chamada da função novamente caso dê erro'''

    print("Dados incorretos")
    limpar()
    acessar_conta()   

  '''Menu interno da conta pessoal'''

  while(resposta != 5):
    if(resposta == 1): #Consulta o saldo
      print(f'\nSaldo: R$ {contas[cpf].saldo}')
      print("-"*40)
      #Exibe menu interno 
      resposta = int(input("1 - Consultar saldo\n2 - Saque\n3 - Deposito\n4 - Alterar senha\n5 - Voltar ao menu\n:"))
 
    elif(resposta == 2): #Saca se estiver dentro das condições
      if(contas[cpf].saldo > 0 or contas[cpf].ehpoupanca == 10): #Verifica se o saldo é maior que 0 no caso da conta poucanca
        valor = float(input("\nValor para saque: "))             #Ou se é conta corrente
        print(contas[cpf].saque(valor))
        print("-"*40)
      else:
        print("\nSaque indisponível!")
        print("-"*40)
      #Exibe menu interno
      resposta = int(input("1 - Consultar saldo\n2 - Saque\n3 - Deposito\n4 - Alterar senha\n5 - Voltar ao menu\n:"))
    
    elif(resposta == 3):
      valor = float(input("\nValor para deposito: "))
      #Checa se depósito é um valor maior que 0
      while(valor < 0):
        print("Digite um valor maior que 0.")
        valor = float(input("\nValor para deposito: "))
      print(contas[cpf].deposito(valor))
      print("-"*40)
      #Exibe menu interno
      resposta = int(input("1 - Consultar saldo\n2 - Saque\n3 - Deposito\n4 - Alterar senha\n5 - Voltar ao menu\n:"))
   
    elif(resposta == 4):
      nova_senha = int(input("\nNova senha: "))
      #Checa se a senha tem 4 digitos
      if(len(str(nova_senha)) == 4):
        contas[cpf].alt_senha(nova_senha) #Método que funciona como setter
        print("Senha alterada.")
        print("-"*40)
        #Exibe menu interno
        resposta = int(input("1 - Consultar saldo\n2 - Saque\n3 - Deposito\n4 - Alterar senha\n5 - Voltar ao menu\n:"))
      
      else:
        print("insira uma senha de 4 digitos\n")
        #Exibe menu interno
        resposta = int(input("1 - Consultar saldo\n2 - Saque\n3 - Deposito\n4 - Alterar senha\n5 - Voltar ao menu\n:"))
    
    elif(resposta == 5):
        limpar()
        menu(4) #Passa valor 4 para não cair no loop de forma errada
        

def menu(res=0):
  '''Função principal que simula um caixa'''

  if res == 0: #Opção padrão que chama o menu de inicio
    res = inicio()

  #Loop que chama as funções correspondentes para as ações que o usuario desejar  
  while(res != 4):
    if(res == 1): 
      if(criar_conta(res) == "S"): #Chama a função criar_conta passando 1 indicando que é do tipo Poupança
        #limpa e volta para o menu
        limpar()
        res = inicio()
      else:
        sair = input("Quando desejar sair digite S: ")
        sair = sair.upper()
        #Condição para voltar ao menu
        while(sair != "S"):
          sair = input("Quando desejar sair digite S: ")
          sair = sair.upper()
        #limpa e volta para o menu
        limpar()
        res = inicio()

    elif(res == 2): 
      if(criar_conta(res) == "S"): #Chama a função criar_conta passando 2 indicando que é do tipo Corrente
        #limpa e volta para o menu
        limpar()
        res = inicio()
      else:
        sair = input("Quando desejar sair digite S: ")
        sair = sair.upper()
        #Condição para voltar ao menu
        while(sair != "S"):
          sair = input("Quando desejar sair digite S: ")
          sair = sair.upper()
        #limpa e volta para o menu
        limpar()
        res = inicio()

    elif(res == 3):
      acessar_conta() #Chama a função acessar_conta que contém um menu interno pessoal
      #limpa e volta para o menu
      limpar()
      res = inicio()
    else:
      res = inicio()

  if(res == 4):
    #limpa e finaliza o sistema
    limpar()
    cabecalho()
    print("\nObrigado por utilizar nosso banco!")
    print("-"*40)

def main():
  '''Testes básicos'''

  print("####-Testes-####")

  #Poupança
  print("\n----Poupança----\n")
  print(f'Nome: {conta1.nome}',end=" ")
  print(f'Conta: {conta1.agencia} {conta1.numero}')
  print(f'Saldo: R$ {conta1.saldo}')
  print(conta1.deposito(1000))
  conta1.rende()
  print(conta1.saque(30))
  print(f'Saldo: R$ {conta1.saldo}')

  #Corrente
  print("\n----Corrente----\n")
  print(f'Nome: {conta2.nome}',end=" ")
  print(f'Conta: {conta2.agencia} {conta2.numero}')
  print(f'Saldo: R$ {conta2.saldo}')
  print(conta2.saque(50))
  print(f'Saldo: R$ {conta2.saldo}')
  print(conta2.deposito(1000))
  print(conta2.saque(30))
  print(f'Saldo: R$ {conta2.saldo}')
  
  '''Modo simulação'''

  simulacao = input("\nDeseja entrar no modo simulação de caixa?(s,n): ")
  simulacao = simulacao.lower()
  if(simulacao == "s"):
    limpar()
    menu()

if(__name__ == '__main__'):
  main()  

