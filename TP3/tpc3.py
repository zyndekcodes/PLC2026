import re
import sys


regras = [
    ("COMENTARIO", r"#[^\r\n]*"),
    ("VARIAVEL", r"\?[^\W_]+"),
    ("LINGUA", r"@[^\s]{2}"),
    ("STRING", r'"[^"\r\n]*"'),
    ("CONCEITO", r"[^\W_]+(?::[^\W_]+)?"),
    ("DELIMITADOR", r"[{}.]"),
    ("ESPACO", r"\s+"),
    ("ERRO", r"."),
]

# [^\W_] corresponde a letras e algarismos, sem o underscore.
padrao = re.compile("|".join(
    f"(?P<{nome}>{expressao})" for nome, expressao in regras
))


def analisar(texto):
    resultado = []

    for token in padrao.finditer(texto):
        tipo = token.lastgroup
        valor = token.group()

        if tipo in ("COMENTARIO", "ESPACO"):
            continue

        if tipo == "ERRO":
            linha = texto.count("\n", 0, token.start()) + 1
            raise ValueError(
                f"Caráter inesperado {valor!r} na linha {linha}."
            )

        if tipo == "CONCEITO":
            if valor == "LIMIT":
                tipo = "LIMIT"
            elif valor.isdecimal():
                tipo = "NUMERO"
                valor = int(valor)
        elif tipo == "STRING":
            valor = valor[1:-1]

        resultado.append((tipo, valor))

    return resultado


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Uso: python3 {sys.argv[0]} ficheiro.txt", file=sys.stderr)
        sys.exit(1)

    try:
        with open(sys.argv[1], "r", encoding="utf-8") as ficheiro:
            tokens = analisar(ficheiro.read())
    except (OSError, ValueError) as erro:
        print(f"Erro: {erro}", file=sys.stderr)
        sys.exit(1)

    for token in tokens:
        print(token)
