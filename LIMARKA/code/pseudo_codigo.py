Pseudo-Codigo Simulated Annealing
Inicio
/* Entradas do Algoritmo */
Ler (S0, M, P, L, alpha)
/* Inicializacao das variaveis */
S = S0
T0 = TempInicial()
T = T0
j = 1
/* Loop principal*/
/* Verifica se foram atendidas as condicoes de termino do algoritmo*/
Repita
    i = 1
    nSucesso = 0
    /* Loop Interno - Realizacao de perturbacao em uma iteracao */
    Repita
        Si = Perturba(S)
        DeltaFi = f(Si) - f(S)
        /* Teste de aceitacao de uma nova solucao */
        Se (Deltafi <= 0) ou (exp(-Deltafi/T) > Randomiza()) entao
            S= Si
            nSucesso = nSucesso + 1
        Fim-se
        i = i + 1
    Ate (nSucesso >= L) ou (i > P)
    /*Atualizacao da Temperatura*/
    T = alpha * T
    /* Atualizacao do Contador de iteracoes */
    j = j + 1
Ate (nSucesso = 0) ou (j > M)
/* Saida do Algoritmo */
Imprima(S)
