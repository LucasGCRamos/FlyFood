import time
from itertools import permutations

# Calcula a distância entre dois pontos
def calcular_distancia(ponto1, ponto2):
    return abs(ponto1[0] - ponto2[0]) + abs(ponto1[1] - ponto2[1])

# Calcula o custo total de uma determinada ordem de entrega
def calcular_custo(ordem, pontos):
    custo_total = 0
    for i in range(len(ordem) - 1):
        ponto_atual = pontos[ordem[i]]
        proximo_ponto = pontos[ordem[i + 1]]
        custo_total += calcular_distancia(ponto_atual, proximo_ponto)
    return custo_total

# Lê a matriz do arquivo e extrai as coordenadas dos pontos
def ler_matriz_arquivo(arquivo):
    pontos = {}

    with open(arquivo, 'r') as file:
        linha = file.readline()
        i = 0
        while linha:
            elementos = linha.strip().split()
            for j, elemento in enumerate(elementos):
                if elemento != '0':
                    pontos[elemento] = (i, j)
            i += 1
            linha = file.readline()

    return pontos

def main():
    nome_arquivo = 'matriz.txt'
    caminho_arquivo = nome_arquivo

    # Carrega a matriz e os pontos do arquivo
    pontos = ler_matriz_arquivo(caminho_arquivo)

    # Lista dos pontos de entrega
    pontos_entrega = list(pontos.keys())

    # Todas as possíveis ordens de entrega
    ordens_possiveis = permutations(pontos_entrega)

    melhor_ordem = None
    menor_custo = float('inf')

    # Encontra a melhor ordem de entrega e calcula o menor custo
    for ordem in ordens_possiveis:
        ordem_com_origem_retorno = ['R'] + list(ordem) + ['R']
        custo_atual = calcular_custo(ordem_com_origem_retorno, pontos)

        if custo_atual < menor_custo:
            menor_custo = custo_atual
            melhor_ordem = ordem_com_origem_retorno

    # Remove 'R' duplicados consecutivos na ordem final
    melhor_ordem_final = [melhor_ordem[0]]
    for ponto in melhor_ordem[1:]:
        if ponto != 'R' or melhor_ordem_final[-1] != 'R':
            melhor_ordem_final.append(ponto)

    print("Melhor ordem de entrega:", melhor_ordem_final)
    print("Menor custo:", menor_custo)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    execution_time = end_time - start_time
    print("Tempo de execução:", execution_time, "segundos")
