from dados import pessoas_cadastradas_lista, idade
import os
from time import sleep

def Mostrar_menu():
        os.system('cls')
        print('-'*30)
        print(' '*7,'MENU PRINCIPAL')
        print('-'*30)
        print('1-Cadastrar nova pessoa')
        print('2-Consultar pessoas cadastradas')
        print('3-excluir usuário cadastrado')
        print('4-sair')
    
def Cadastrar_Nova_Pessoa():
    try:
        os.system('cls')
        print('-'*22)
        print('Cadastrar nova pessoa')
        print('-'*22)
        nome_da_pessoa_cadastrada = str(input('Digite o nome da pessoa:')).capitalize()
        idade_da_pessoa_cadastrada =int(input('Digite a sua idade:'))
        if nome_da_pessoa_cadastrada=='':
            nome_da_pessoa_cadastrada='Desconhecido'
        pessoas_cadastradas_lista.append(nome_da_pessoa_cadastrada)
        idade.append(idade_da_pessoa_cadastrada)
           
        print('Usuário cadastrado com sucesso!')

    except:
        print('Valor inválido, erro na digitação')
    input('\nDigite uma tecla para voltar ao menu principal')

def Pessoas_Cadastradas():
        os.system('cls')
        print('-'*30)
        print('Ver pessoas cadastradas')
        print('-'*30)
        for nome_idade in range(len(pessoas_cadastradas_lista)):
            print('Nome:',pessoas_cadastradas_lista[nome_idade],' '*10 ,'Idade:',idade[nome_idade],'Anos')
        input('\nDigite uma tecla para voltar ao menu principal')

def Excluir_Pessoa_Cadastrada():
        os.system('cls')
        print('-'*30)
        print('excluir usuário cadastrado')
        print('-'*30)
        pessoa_excluida=str(input('Qual pessoa deseja excluir?')).capitalize()
        if pessoa_excluida in pessoas_cadastradas_lista:
            pessoas_cadastradas_lista.remove(pessoa_excluida)
            print('Usuario excluido com sucesso!')

        else:
            print('Usuario não encontrado!')
        input('\nDigite uma tecla para voltar ao menu principal')

def Encerrar_programa():
        os.system('cls')
        print('ENCERRANDO PROGRAMA...')
        sleep(2.3)
        os.system('cls')

def Opcao_invalida():
    os.system('cls')
    print('ERRO!')
    input('Digite uma tecla para voltar ao menu principal:')

        


