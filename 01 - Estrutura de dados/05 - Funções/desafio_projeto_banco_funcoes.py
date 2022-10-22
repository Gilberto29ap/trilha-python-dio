
import time
import os




def menu_inicial():#menu inicial

    carregamento()

    os.system('cls' if os.name == 'nt' else 'clear') #limpa tela

    title = "Bem vindo ao BANCO PYTHON"

    for letter in title:
        
        print(letter, end=" ")

    print("""
    Digite a opção desejada e pressione ENTER
            [s]     SAQUE
            [e]     EXTRATO
            [d]     DEPÓSITO
            [nc]    NOVA CONTA
            [lc]    LISTAR CONTA
            [nu]    NOVO USUÁRIO
            [q]     SAIR
    """)

def carregamento(): #define um delay para abrir o menu inicial e anima um carregamento
    tempo_carregamento = 3
    for i in range(tempo_carregamento):
        if i <= tempo_carregamento:
            print(".")
            time.sleep(0.25)

def saque(*, LIMITE_POR_SAQUE, NUMERO_MAX_SAQUE, saldo, extrato, saque_do_dia):
    print("--------SAQUE--------")
    valor_saque = int(input("digite o valor: "))

    if valor_saque > 0: 
        if saque_do_dia <= NUMERO_MAX_SAQUE:
            if valor_saque <= LIMITE_POR_SAQUE:
                if valor_saque <= saldo:
                    print("Efetuando saque, por favor aguarde!")
                    carregamento()
                    print("Saque efetuado com sucesso!")
                    input("Pressione enter para sair")
                    menu_inicial()
                        
                    saldo -= valor_saque
                    saque_do_dia += 1
                    extrato += f"\nSaque       -R$ {valor_saque:.2f}"

                    return extrato, saldo, saque_do_dia

                    
                    
                else:
                    print(f"Saldo insuficiente, seu saldo atual é de: {saldo}")
                    input("Pressione enter para sair")
                    menu_inicial()

                    return extrato, saldo, saque_do_dia

            else: 
                print("O limite máximo para saques é R$ 500")
                input("Pressione enter para sair")
                menu_inicial()

                return extrato, saldo, saque_do_dia
                    
        else:
            print("Número de saques diários excedido. Tente Novamente amanhã")
            input("Pressione enter para sair")
            menu_inicial()

            return extrato, saldo, saque_do_dia

    else:
        print("Valor inválido")
        menu_inicial()
        return extrato, saldo, saque_do_dia


def extrato_funcao(extrato, /, *, saldo):
    print("--------EXTRATO--------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo        R$ {saldo:.2f}")
    input("Pressione enter para sair")
    menu_inicial()

def deposito(extrato, saldo, /):
    print("--------DEPÓSITO-------")
    deposito_valor = int(input("Digite o valor a ser depositado: "))

    if deposito_valor > 0:
        print(f"depósito de R$ {deposito_valor:.2f} efetuado com sucesso!")
        extrato += f"\nDepósito    +R$ {deposito_valor:.2f}"
        input("Pressione enter para sair")
        saldo += deposito_valor
        menu_inicial()
        return extrato, saldo

    else:
        print("Valor inválido")
        input("Pressione enter para sair")
        menu_inicial()
        return extrato, saldo

def filtrar_usuario(usuarios, cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario_repetido = filtrar_usuario(usuarios, cpf)

    if usuario_repetido:
        print("Já existe um usuário com este CPF")
        menu_inicial()
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereco (Rua, nro - Bairro - Cidade/UF): ")
    usuarios.append({"nome": nome, "data de nascimento": data_nascimento,  "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")
    menu_inicial()

def criar_conta(agencia, numero_conta, usuarios):
    CPF = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(usuarios, CPF)

    if usuario:
        print("\nConta criada com sucesso!")
        menu_inicial()
        return {"Agência":agencia, "Número da conta": numero_conta, "usuario": usuario}
    else: print("Este usuário não existe!")
    menu_inicial()

def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência:    {conta["Agência"]}
        Conta:      {conta["Número da conta"]}
        Titular:    {conta["usuario"]["nome"]}
        CPF:        {conta["usuario"]["cpf"]}

        ================================================        
        
        """
        print(linha)
    input("Pressione enter para continuar")

    menu_inicial()

def main():
    LIMITE_POR_SAQUE = 500
    NUMERO_MAX_SAQUE = 3
    saldo = 1000
    extrato = ""
    saque_do_dia = 1
    usuarios = []
    AGENCIA = "0001"
    contas = []
    
    while True:
        opcao = input("Digite a opção desejada: ")

        os.system('cls' if os.name == 'nt' else 'clear')    #limpa tela

        if opcao == "s":                                    #chama da para funcao saque
            extrato, saldo, saque_do_dia = saque(           #função com passagem nomeada de parametros
                LIMITE_POR_SAQUE = LIMITE_POR_SAQUE,
                NUMERO_MAX_SAQUE = NUMERO_MAX_SAQUE,
                saldo = saldo,
                extrato = extrato,
                saque_do_dia = saque_do_dia)
    

        elif opcao == "e":
            extrato_funcao(extrato, saldo = saldo)


        elif opcao == "d":                                  #chamada para funcao deposito
            extrato, saldo = deposito(extrato, saldo)       #funcao com passagem de parametros por posicao

        elif opcao == "nc":
            print("-------NOVA CONTA-------")
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            print("-------LISTAR CONTAS-------")
            listar_contas(contas)

        elif opcao == "nu":
            print("-------NOVO USUÁRIO-------")
            criar_usuario(usuarios)


        elif opcao == "q":
            print("Obrigado por utilizar o BANCO PYTHON!")
            time.sleep(1)
            break


        else:
            print("Opção inválida, tente novamente")
            menu_inicial()

menu_inicial()

main()
