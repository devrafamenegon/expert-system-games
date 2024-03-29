# Sistema Especialista em Recomendação de Jogos 🕹️

## Objetivo do Projeto

O Sistema Especialista para Recomendação de Jogos é um sistema desenvolvido com o objetivo de auxiliar os usuários na escolha de jogos eletrônicos com base em seus gostos pessoais. Utilizando técnicas de inteligência artificial, o sistema analisa os gêneros de jogos indicados pelo usuário e fornece recomendações personalizadas, classificando os jogos disponíveis em um banco de dados de acordo com sua relevância para os interesses do usuário.

## Funcionamento do Sistema

### Coleta de Dados

O sistema inicia zerando as ocorrências e percentuais no banco de dados, garantindo que os cálculos sejam feitos corretamente. Em seguida, ele solicita ao usuário que indique os gêneros de jogos de seu interesse, bem como o grau de importância de cada gênero indicado.

### Processamento de Dados

Após a coleta dos dados fornecidos pelo usuário, o sistema realiza o processamento das informações. Ele compara os gêneros indicados pelo usuário com os gêneros dos jogos disponíveis no banco de dados, levando em consideração o grau de importância atribuído a cada gênero pelo usuário. Com base nessa comparação, o sistema calcula as ocorrências de cada jogo e seu percentual de matching em relação aos interesses do usuário.

### Recomendação de Jogos

Com as ocorrências e percentuais calculados, o sistema ordena os jogos do banco de dados de acordo com seu percentual de matching, apresentando ao usuário uma lista de jogos recomendados, organizados de forma decrescente em relação à sua relevância para os interesses indicados.

## Objetivo

o Sistema Especialista para Recomendação de Jogos visa simplificar a busca por novos jogos, proporcionando aos usuários uma maneira eficiente e personalizada de descobrir títulos que correspondam aos seus interesses e preferências.

# Feito por Rafael Menegon
