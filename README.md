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
    python -m chunker <nome_do_arquivo.txt> <número de iterações> <morph>
```

Caso queira fazer parser morfológico, utilizar o parâmetro *morph*:

Exemplo: 
```
    python -m chunker texto.txt 50 
```

Exemplo (morfológico):
```
    python -m chunker texto.txt 50 morph
```