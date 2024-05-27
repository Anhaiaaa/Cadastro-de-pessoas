import os
from funcoes import Cadastrar_Nova_Pessoa, Pessoas_Cadastradas, Excluir_Pessoa_Cadastrada, Mostrar_menu, Encerrar_programa, Opcao_invalida
from dados import idade,pessoas_cadastradas_lista
while True:
    try:
        Mostrar_menu()
        opcao = int(input('Digite uma opção:'))
        if opcao==1:
                Cadastrar_Nova_Pessoa()
                    
        elif opcao==2:
                Pessoas_Cadastradas()
                
        elif opcao==3:
                Excluir_Pessoa_Cadastrada()
                    
        elif opcao==4:
            Encerrar_programa()
            break

        elif opcao>4:
              Opcao_invalida()
                
    except ValueError:
        os.system('cls')
        print('ERRO!')     
        input('Digite uma tecla para voltar ao menu principal:')
   