frase = "Esta é a frase inicial"
lista1 = [0,0]

def iteracao_deep(frase):
    for i in range(3):
        frase += f"\n linha da iteração {i+1}"
    return frase
        

def iteracao_lista(lista1):
    for i in range (3):
        lista1.append(i+3)



def main(frase, lista1):
    iteracao_lista(lista1)
    frase = iteracao_deep(frase)
    print(f"Abaixo a frase após iteração\n{frase}")
    print(lista1)

main(frase, lista1)




