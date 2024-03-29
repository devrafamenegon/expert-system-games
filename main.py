from unidecode import unidecode
from utils import indique_genero, indique_grau, deseja_adicionar_genero
from database import BD, zerar_ocorrencias, mostrar_generos

# ZERAR OCORRENCIAS E PERCENTUAIS NO BANCO DE DADOS
zerar_ocorrencias()

# INICIALIZAR VARIÁVEIS
generosIndicados = []
continuar = True

mostrar_generos()

# COLETAR DADOS
while continuar:
    generosIndicados.append((indique_genero(), indique_grau()))
    continuar = deseja_adicionar_genero()

# CALCULAR OCORRÊNCIAS
for jogo in BD:
    for generoIndicado, grauIndicado in generosIndicados:
        for jogo_genero in jogo["GENERO"]:
            if unidecode(jogo_genero["NOME"].lower()) == unidecode(generoIndicado.lower()):
                jogo["OCORRENCIAS"] += grauIndicado * jogo_genero["GRAU"]

# MOSTRAR GÊNEROS INDICADOS
print("\n*************************************")
print("\nRESULTADOS PARA OS GÊNEROS: ")
for generoIndicado, grauIndicado in generosIndicados:
    print(f" - {generoIndicado} (Grau: {grauIndicado})")

# ENCONTRAR A MAIOR OCORRÊNCIA
maior_ocorrencia = max(jogo["OCORRENCIAS"] for jogo in BD)

# CALCULAR PERCENTUAL
for jogo in BD:
    jogo["PERCENTUAL"] = (jogo["OCORRENCIAS"] / maior_ocorrencia) * 100

# ORDENAR JOGOS POR PERCENTUAL DE MATCHING
jogos_ordenados = sorted(BD, key=lambda x: x["PERCENTUAL"], reverse=True)

# MOSTRAR JOGOS ORDENADOS
print("\nJOGOS ORDENADOS POR PERCENTUAL DE MATCHING:")
for jogo in jogos_ordenados:
    print(f"{jogo['PERCENTUAL']:.2f}% = {jogo['TITULO']}")
