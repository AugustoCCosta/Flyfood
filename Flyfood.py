from time import process_time
soma_tempo = 0
for _ in range(30):
    comeco = process_time()

    arquivo = open('entrada9.txt', 'r')

    n, m = arquivo.readline().split()
    linhas = arquivo.read().splitlines()

    ponto_org = []
    coords = []

    # Pega os pontos e coordenadas
    for i in range(int(n)):
        linha = linhas[i].split()
        for j in range(int(m)):
            if linha[j] != '0':
                if linha[j] == 'R':
                    ponto_org.append([i, j])
                else:
                    coords.append([i, j])

    # Realiza a permutação dos pontos de entrega
    def permutacao(pontos):
        if len(pontos) <= 1:
            return [pontos]
        permutacoes = []
        for index in range(len(pontos)):
            elem_fixo = pontos[index]
            lista_solta = pontos[:index] + pontos[index + 1:]
            for p in permutacao(lista_solta):
                permutacoes.append([elem_fixo] + p)
        return permutacoes

    caminhos = permutacao(coords)
    # print(caminhos)

    # Calcula a distância entre os pontos
    def distancia(pi, pj):
        dist = abs(pi[0] - pj[0]) + abs(pi[1] - pj[1])
        return dist

    menor_custo = float('inf')
    melhor_caminho = None

    for caminho in caminhos:
        saida = distancia(ponto_org[0], caminho[0])
        volta = distancia(caminho[len(caminho)-1], ponto_org[0])
        custo = 0
        for ponto_i in range(len(caminho)-1):
            soma = distancia(caminho[ponto_i], caminho[ponto_i+1])
            custo += soma
        custo_total = custo + saida + volta
        if custo_total < menor_custo:
                menor_custo = custo_total
                melhor_caminho = caminho

    # Pegando as posições do melhor caminho
    melhor_perc = []
    for posicao in melhor_caminho:
        linha, coluna = posicao
        ponto = linhas[linha].split()[coluna]
        melhor_perc += ponto

    print(menor_custo, melhor_perc)

    fim = process_time()
    tempo = (fim - comeco)
    soma_tempo += tempo


print(f"O tempo de execução foi: {soma_tempo/30} segundos")
