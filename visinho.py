import time

def calcular_distancia(ponto1, ponto2):
    return abs(ponto1[0] - ponto2[0]) + abs(ponto1[1] - ponto2[1])

def encontrar_proximo_ponto(atual, pontos, visitados):
    menor_distancia = float('inf')
    proximo_ponto = None
    for ponto, coordenadas in pontos.items():
        if ponto not in visitados:
            distancia = calcular_distancia(atual, coordenadas)
            if distancia < menor_distancia:
                menor_distancia = distancia
                proximo_ponto = ponto
    return proximo_ponto

def calcular_custo(ordem, pontos):
    custo_total = 0
    for i in range(len(ordem) - 1):
        ponto_atual = pontos[ordem[i]]
        proximo_ponto = pontos[ordem[i + 1]]
        custo_total += calcular_distancia(ponto_atual, proximo_ponto)
    return custo_total

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

    pontos = ler_matriz_arquivo(nome_arquivo)

    ordem = ['R']
    visitados = set(['R'])

    while len(visitados) < len(pontos):
        ponto_atual = ordem[-1]
        proximo_ponto = encontrar_proximo_ponto(pontos[ponto_atual], pontos, visitados)
        ordem.append(proximo_ponto)
        visitados.add(proximo_ponto)

    ordem.append('R')

    custo_final = calcular_custo(ordem, pontos)

    print("Ordem de entrega usando vizinho mais próximo:", ordem)
    print("Custo total:", custo_final)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    execution_time = end_time - start_time
    print("Tempo de execução:", execution_time, "segundos")