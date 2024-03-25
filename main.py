from utils import indique_genero, indique_grau, deseja_adicionar_genero
from database import BD, zerar_ocorrencias, mostrar_generos

zerar_ocorrencias()

generosIndicados = []
continuar = True

mostrar_generos()

while continuar:
    generosIndicados.append((indique_genero(), indique_grau()))
    continuar = deseja_adicionar_genero()

# CALCULAR OCORRÊNCIAS
for jogo in BD:
    for generoIndicado, grauIndicado in generosIndicados:
        for jogo_genero in jogo["GENERO"]:
            if jogo_genero["NOME"] == generoIndicado:
                jogo["OCORRENCIAS"] += grauIndicado * jogo_genero["GRAU"]

# VERIFICAÇÃO DE MATCHING CONSIDERANDO O TOTAL DE GENEROS
print("\n*************************************")
print("\nRESULTADOS PARA OS GÊNEROS: ")

for generoIndicado, grauIndicado in generosIndicados:
    print(f" - {generoIndicado} (Grau: {grauIndicado})")

print("\nPROBABILIDADE DE MATCHING CONSIDERANDO O TOTAL DE GÊNEROS: ")

# Encontrar a maior ocorrência
maior_ocorrencia = max(jogo["OCORRENCIAS"] for jogo in BD)

for jogo in BD:
    jogo["PERCENTUAL"] = (jogo["OCORRENCIAS"] / maior_ocorrencia) * 100
    print(f"{jogo['PERCENTUAL']:.2f}% = {jogo['TITULO']}")

# ORDENAR JOGOS POR PERCENTUAL DE MATCHING
jogos_ordenados = sorted(BD, key=lambda x: x["PERCENTUAL"], reverse=True)

print("\nJOGOS ORDENADOS POR PERCENTUAL DE MATCHING:")
for jogo in jogos_ordenados:
    print(f"{jogo['PERCENTUAL']:.2f}% = {jogo['TITULO']}")
