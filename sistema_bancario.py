#Constantes
NUMERO_MAXIMO_SAQUES = 3
LIMITE_SAQUE = 500

# Variáveis
saldo = 0
deposito = -1
tentar_novamente = "s"
extrato = ""
saque = -1
numero_de_saques = 0
menu = """
 **** Menu ****

 (d) Depósito
 (s) Saque
 (e) Extrato
 (q) Sair 

 Digite a opcao desejada: """

mensagem_erro_redigitacao = """
 Gostaria de digitar outro valor ?
 (s) Sim
 (n) Não

 Digite sua escolha: """

# Repetição do menu enquanto a opção de saída não é requisitada
while True:
    opcao = input(menu)

    # Depósito
    if opcao == "d":
        # Loop para que o cliente possa digitar um novo valor em caso de erro no depósito
        while deposito < 0 and tentar_novamente == "s":
            print( "\n **** Depósito **** ")
            deposito = input("\n Digite o valor que deseja depositar: ")
            deposito = float(deposito)
            # O depósito apenas é efetuado para valores positivos
            if deposito > 0:
                saldo += deposito
                print(f"\n Depósito realizado com sucesso! Saldo Atual: R${saldo:.2f}") 
                extrato += f" Operação: Depósito, Valor: {deposito} \n"
            else:
                # Tratamento de erro em depósitos
                print("\n Erro! Valor de depósito inválido")
                tentar_novamente = input(mensagem_erro_redigitacao)
                if tentar_novamente != "n" and tentar_novamente != "s":
                    print("\n Opcao Inválida! Retornaremos-lhe ao menu")
                    tentar_novamente = "n"
        else: #Restaurando os valores das variáveis para um novo depósito
            deposito = -1
            tentar_novamente = "s"
    
    # Extrato
    elif opcao == "e":
        print("\n **** Extrato ****\n")
        print(extrato)
        print(f" Saldo Atual: R$ {saldo:.2f}")

    #Saque 
    elif opcao == "s":
        # Loop para que o cliente possa digitar um novo valor em caso de erro no saque
        while saque < 0 and tentar_novamente == "s":
            # Verificação da quantidade de saques diários
            if numero_de_saques < NUMERO_MAXIMO_SAQUES:
                print( "\n **** Saque **** ")
                saque = input("\n Digite o valor que deseja sacar: ")
                saque = float(saque)
                # O saque apenas é efetuado para valores positivos 
                if saque > 0:
                    if saque <= LIMITE_SAQUE:
                        if saque <= saldo:
                            saldo -= saque
                            print(f"\n Saque realizado com sucesso! Saldo Atual: R${saldo:.2f}") 
                            extrato += f" Operação: Saque, Valor: {saque}\n"
                            numero_de_saques += 1
                        else:
                            # Tratamento do erro de saldo insuficiente
                            print(f"\n Erro! Saldo Insuficiente. Saldo atual: R${saldo:.2f}")
                            tentar_novamente = input(mensagem_erro_redigitacao)
                            if tentar_novamente != "n" and tentar_novamente != "s":
                                print("\n Opcao Inválida! Retornaremos-lhe ao menu")
                                tentar_novamente = "n"
                            else:
                                saque = -1   
                    else: 
                          # Tratamento do erro de saque maior que o limite
                            print(f"\n Erro! O limite de saque é de {LIMITE_SAQUE}")
                            tentar_novamente = input(mensagem_erro_redigitacao)
                            if tentar_novamente != "n" and tentar_novamente != "s":
                                print("\n Opcao Inválida! Retornaremos-lhe ao menu")
                                tentar_novamente = "n"
                            else:
                                saque = -1  
                else: 
                    # Tratamento de erro em saques inválidos
                    print("\n Erro! Valor de saque inválido")
                    tentar_novamente = input(mensagem_erro_redigitacao)
                    if tentar_novamente != "n" and tentar_novamente != "s":
                        print("\n Opcao Inválida! Retornaremos-lhe ao menu")
                        tentar_novamente = "n"
                    else:
                        saque = -1
            else:
                # Tratamento do erro de limite de saque diário atingido
                print(f"\n Erro! A quantidade máxima de {NUMERO_MAXIMO_SAQUES} saques diários foi atingida ")
                tentar_novamente = "n"
        else: #Restaurando os valores das variáveis para um novo saque
            saque = -1
            tentar_novamente = "s"

    #Saída
    if opcao == "q":
        print("\n Obrigado por usar nossos serviços!")
        break
