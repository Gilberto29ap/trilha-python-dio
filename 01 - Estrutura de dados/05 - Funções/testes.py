from numpy import true_divide


print("Bem vindo ao adivinhador de números")

def checagem_numero(numero):
    checagem_numero = numero > 0 or numero is int
    return  checagem_numero


numero_original = input("Digite um número para eu adivinhar:")


if checagem_numero(numero_original):
    #limpar tela
    print("Ok armazenei o número, agora peça para outra pessoa adivinhar")
    while True:
        novo_numero = input("Adivinhe o número:")
        if novo_numero == numero_original:
            print("Uhuuu! Você acertou!")

        elif checagem_numero(novo_numero):
            diferenca_numeros = numero_original - novo_numero if numero_original > novo_numero else novo_numero - numero_original
            temperatura = "muito quente!" if diferenca_numeros < 10 else "quente" if diferenca_numeros < 50 else "frio"
            altura = "mais baixo" if novo_numero > numero_original else "mais alto"
            print(f"Está {temperatura}!, tente um número mais {altura}")
            
        else:
            print("Número inválido, tente novamente:")

    
else:
    print("Número inválido, tente outra vez")



