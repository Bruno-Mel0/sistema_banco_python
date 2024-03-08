print(" Bem vindo ao D.I.O.CRED")

saldo = float(2000) 
limite_por_saque = float(500) 
extrato = ""
saques = 0
LIMITES_SAQUES_DIARIOS = 3
menu_inicial = '''
========== MENU ==========

      [1] Depósito
      [2] Saque
      [3] Extrato
      [0] Sair

==========================
'''
menu_retorno = '''
==========================
[1] Voltar ao menu inicial
[0] Sair
==========================
'''
while True: 
    
    opcao_inicial = input(menu_inicial)
    if opcao_inicial == "1":
        valor = float(input("Qual valor deseja depositar ?"))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito de: {valor:.2f}\n"
            print("Deposito realizado com sucesso.")
            opcao = input(menu_retorno)
            if opcao == "1":
                opcao_inicial
            elif opcao == "0":
                print("Obrigado por usar nosso banco.")
                break
            else:
              print("ERRO !! \nSelecione a opção desejada.")                                       
        else:
            print("ERRO !! \nInsira um valor válido.")
            opcao = input(menu_retorno)
            if opcao == "1":
                opcao_inicial
            elif opcao == "0":
                print("Obrigado por usar nosso banco.")
                break
            else:
                print("ERRO !! \nSelecione a opção desejada.")

    elif opcao_inicial == "2":
        valor = float(input("Qual valor deseja sacar ?"))
        excedeu_valor = valor > saldo
        excedeu_limite = valor > limite_por_saque
        excedeu_saques = saques >= LIMITES_SAQUES_DIARIOS
        
        if excedeu_valor:
            print("ERRO !! \nSaldo insuficiente.\n")
            opcao = input(menu_retorno)
            if opcao == "1":
                opcao_inicial
            elif opcao == "0":
                print("Obrigado por usar nosso banco.")
                break
            else:
                print("ERRO !! \nSelecione a opção desejada.")

        elif excedeu_limite:
            print("ERRO !! \nO valor excede o limite por saque.")
            opcao = input(menu_retorno)
            if opcao == "1":
                opcao_inicial
            elif opcao == "0":
                print("Obrigado por usar nosso banco.")
                break
            else:
                print("ERRO !! \nSelecione a opção desejada.")
        
        elif excedeu_saques:
            print("ERRO !! \nNúmero de saques diários excedidos.")
            opcao = input(menu_retorno)
            if opcao == "1":
                opcao_inicial
            elif opcao == "0":
                print("Obrigado por usar nosso banco.")
                break
            else:
                print("ERRO !! \nSelecione a opção desejada.")
        
        elif valor > 0:
            saldo -= valor
            saques += 1
            extrato += f"Saque de: {valor:.2f}\n"
            print("Saque realizado com sucesso.")
            opcao = input(menu_retorno)
            if opcao == "1":
                opcao_inicial
            elif opcao == "0":
                print("Obrigado por usar nosso banco.")
                break
            else:
                print("ERRO !! \nSelecione a opção desejada.")
        
        else:
            print("ERRO !! \nValor informado não é válido")
    
    elif opcao_inicial == "3":
        print('''***** EXTRATO *****''')
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"""==> Saldo: R$ {saldo:.2f}""")
        print("""****************""")
        opcao = input(menu_retorno)
        if opcao == "1":
            opcao_inicial
        elif opcao == "0":
            print("Obrigado por usar nosso banco.")
            break
        else:
            print("ERRO !! \nSelecione a opção desejada.")
      
    elif opcao_inicial == "0":
        print("Obrigado por usar nosso banco.")
        break
    
    else:
        print("ERRO !! \nSelecione a opção desejada.")
        
    

    


            
            

       

    
        
         
    
         

      

