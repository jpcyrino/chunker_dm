# chunker_dm
 Implementação em python do chunker de Carl de Marcken

## Instalação:

- Clonar o repositório
- Criar ambiente virtual (dentro da pasta chunker_dm)

```
    python -m venv venv
```

- Ativar o ambiente virtual

```
    venv\scripts\activate
```

- Instalar os requisitos

```
    pip install -r requirements.txt
```

## Executar:

```
    python -m chunker <nome_do_arquivo.txt> <número de iterações> <número de novas plavras> <morph>
```

Caso queira fazer parser morfológico, utilizar o parâmetro *morph*:

Exemplo: 
```
    python -m chunker texto.txt 50 25
```

Exemplo (morfológico):
```
    python -m chunker texto.txt 50 25 morph
```

O chunker gerará três arquivos:

- lexicon.csv: o léxico contendo os itens lexicais encontrados seguido do logaritmo positivo de sua probabilidade no corpus
- lexicon.txt: os morfemas descobertos
- segmented.txt: a lista de palavras segmentadas


## Exemplo com os dados do Kikongo:

```
    python -m chunker kikongo.txt 25 80 morph
```

Gerará três arquivos:

- details.csv: métricas do parser
- lexicon.txt: os morfemas descobertos
- segmented.txt: a lista de palavras segmentadas

## Avaliação do modelo com dados do ocun:

```
    python -m evaluate daw.txt 
```

Exibirá os parâmetros para 10, 25, 50, 100, 500, 1000, 5000 e 10000 novos morfemas por iteração

## ocun.py

Prepara arquivos do ocun:

```
    python -m ocun <arquivo_entrada> <arquivo_saida>
```
```