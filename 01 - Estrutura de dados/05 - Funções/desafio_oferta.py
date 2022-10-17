
T = int(input())

for i in range(T):
    entrada = input()
    N = int(entrada.split()[0])
    K = int(entrada.split()[1])

    garrafa_ganhada = int(N/K)
    garrafa_sobra = N%K

    total_prox_dia = garrafa_ganhada + garrafa_sobra

    print(total_prox_dia)
    

