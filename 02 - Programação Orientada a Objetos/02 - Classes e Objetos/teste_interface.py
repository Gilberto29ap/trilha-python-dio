import random
from tkinter import *

numero_testes = 100000


def teste_trocando():
    # numero_testes = 2000
    acertou = 0
    errou = 0
    
    for i in range(numero_testes):
        portas = ["A", "B", "C"]                #Inicio do processo, zeragem da lista
        portas_copy = portas.copy()             #Criacao da copia da lista original
        porta_premio = random.choice(portas)    #Randorizacao da porta que vai estar o premio
        porta_escolhida = random.choice(portas) #Selecao da porta do usuario
        if porta_premio == porta_escolhida:     #verificando se porta escolhida é a mesma do premeio
            portas_copy.remove(porta_premio) 
        else:
            portas_copy.remove(porta_premio)
            portas_copy.remove(porta_escolhida)

        #mostrar porta sem o premio e dar opcao de troca
        porta_revelada = random.choice(portas_copy)
        
        #se nao trocar, nada a fazer
        
        #se trocar, remorver a porta revelada e a porta escolhida da lista e atualizar valor da porta escolhida
        portas.remove(porta_revelada)
        portas.remove(porta_escolhida)

        porta_escolhida = portas[0]                  #atualizando valor da porta escolhida

        

        texto_processamento1 = f"Porta escolhida: {porta_escolhida}"
        texto_processamento2 = f"Porta da cabra: {porta_premio}"

        if porta_escolhida == porta_premio:
            texto_processamento3 = "Acertou"
            acertou += 1

        else:
            texto_processamento3 = "Errou"
            errou += 1
        # resultado_testes = f"{texto_processamento1}\n{texto_processamento2}\n{texto_processamento3}"

    texto = f"Número de acertos:{acertou}\nNúmero de erros:{errou}"
    resultado_testes["text"] = texto

# teste_trocando()
exec_teste = teste_trocando
    
janela1 = Tk()
janela1.title("Teste do paradoxo de monty hall")

texto_explicativo = Label(janela1, text = f"Explicação do paradoxo")
texto_explicativo.grid(column = 0, row = 0, padx=10, pady=10)

texto_cabecalho = Label(janela1, text = f"Executando {numero_testes} testes com troca de portas")
texto_cabecalho.grid(column = 0, row = 1, padx=10, pady=10)

botao1 = Button(janela1, text="Executar testes", command=exec_teste)
botao1.grid(column=0, row=3, padx=10, pady=10)

resultado_testes = Label(janela1, text="")
resultado_testes.grid(column=0, row=4, padx=10, pady=10)




janela1.mainloop()