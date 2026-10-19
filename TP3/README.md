# TP3

Aluno: Gonçalo Silva Faria  
Id: A104942

<img src="pfp-plc.png" width="80">

## Enunciado

Construir um analisador léxico para uma linguagem de query, capaz de reconhecer:

- Variáveis iniciadas por `?`;
- Identificadores de língua iniciados por `@`, seguidos de dois carateres;
- Strings entre aspas;
- Identificadores de conceitos;
- Os delimitadores `{`, `}` e `.`;
- A palavra reservada `LIMIT`;
- Valores numéricos.

Os comentários iniciados por `#` devem ser ignorados até ao fim da linha.

## Resumo

Neste trabalho foi desenvolvido um analisador léxico em Python utilizando expressões regulares. O programa ignora comentários e espaços e apresenta um par `(tipo, valor)` por token.

Os identificadores aceitam letras e algarismos, sem underscores. Os nomes com prefixo, como `dbo:MusicalArtist`, são reconhecidos como um único conceito, para permitir processar o exemplo do enunciado. Apenas `LIMIT` é reservada, distinguindo maiúsculas de minúsculas; `select`, `where` e `a` são conceitos.

Os identificadores de língua são lidos como `@` seguido de dois carateres sem espaços. Consideram-se strings entre aspas duplas, numa só linha e sem escapes, e números inteiros não negativos. Um caráter não reconhecido provoca uma mensagem de erro com a linha e termina a execução.

Para executar a partir da raiz do repositório, apenas com Python 3:

```bash
python3 TP3/tpc3.py TP3/teste.txt
```

## Resultados

- [Programa Python](tpc3.py)
- [Ficheiro de teste](teste.txt)
- [Resultado da análise](resultado.txt)