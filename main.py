from utils import *
from database import *

zerar_ocorrencias()

generosIndicados = []
ler = True

mostrar_generos()

while ler:
    generosIndicados.append((indique_genero(), indique_grau()))
    ler = deseja_adicionar_genero()

# CALCULAR OCORRÊNCIAS
for jogo in BD:
    for generoIndicado, grauIndicado in generosIndicados:
        for jogo_genero in jogo["GENERO"]:
            if jogo_genero["NOME"] == generoIndicado:
                jogo["OCORRENCIAS"] += grauIndicado * jogo_genero["GRAU"]
                print(jogo["OCORRENCIAS"])

# VERIFICAÇÃO DE MATCHING CONSIDERANDO O TOTAL DE GENEROS
print("\n*************************************")
print("\nRESULTADOS PARA OS GÊNEROS: ")

for generoIndicado, grauIndicado in generosIndicados:
    print(f" - {generoIndicado} (Grau: {grauIndicado})")

print("\nPROBABILIDADE DE MATCHING CONSIDERANDO O TOTAL DE GENEROS: ")

for jogo in BD:
    total_generos = sum(
        grau * genero["GRAU"]
        for genero, grau in generosIndicados
        for genero in jogo["GENERO"]
        if genero["NOME"] == genero
    )
    percentual_matching = (
        (jogo["OCORRENCIAS"] / total_generos) * 100 if total_generos > 0 else 0
    )

    jogo["PERCENTUAL"] = percentual_matching

    print(f"{percentual_matching:.2f}% = {jogo['TITULO']}")

# ORDENAR JOGOS POR PERCENTUAL DE MATCHING
jogos_ordenados = sorted(BD, key=lambda x: x["PERCENTUAL"], reverse=True)

print("\nJOGOS ORDENADOS POR PERCENTUAL DE MATCHING:")
for jogo in jogos_ordenados:
    print(f"{jogo['PERCENTUAL']:.2f}% = {jogo['TITULO']}")
