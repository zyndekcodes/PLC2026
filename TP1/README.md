# TP1

Aluno: Gonçalo Faria  
Id: A104942

<img src="pfp-plc.png" width="80">

## Enunciado

Escrever uma expressão regular que reconheça strings binárias que não contenham a substring `011`.

## Resolução

```regex
^1*(0|01)*$
```