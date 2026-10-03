import re
import sys


def inline_to_html(texto):
    # Imagens
    texto = re.sub(
        r'!\[([^\]]*)\]\(([^)]+)\)',
        r'<img src="\2" alt="\1"/>',
        texto
    )

    # Links
    texto = re.sub(
        r'\[([^\]]+)\]\(([^)]+)\)',
        r'<a href="\2">\1</a>',
        texto
    )

    # Bold
    texto = re.sub(
        r'\*\*([^*]+)\*\*',
        r'<b>\1</b>',
        texto
    )

    # Itálico
    texto = re.sub(
        r'\*([^*]+)\*',
        r'<i>\1</i>',
        texto
    )

    return texto


def markdown_to_html(texto):
    linhas = texto.splitlines()
    resultado = []
    em_lista = False

    for linha in linhas:

        # Lista numerada
        item = re.match(r'^\d+\.\s+(.*)$', linha)

        if item:
            if not em_lista:
                resultado.append("<ol>")
                em_lista = True

            conteudo = inline_to_html(item.group(1))
            resultado.append(f"<li>{conteudo}</li>")
            continue

        # Se a lista acabou, fecha o <ol>
        if em_lista:
            resultado.append("</ol>")
            em_lista = False

        # Cabeçalhos
        cabecalho = re.match(r'^(#{1,3})\s+(.*)$', linha)

        if cabecalho:
            nivel = len(cabecalho.group(1))
            conteudo = inline_to_html(cabecalho.group(2))
            resultado.append(
                f"<h{nivel}>{conteudo}</h{nivel}>"
            )
        else:
            resultado.append(inline_to_html(linha))

    # Caso o ficheiro termine dentro de uma lista
    if em_lista:
        resultado.append("</ol>")

    return "\n".join(resultado)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Uso: python3 {sys.argv[0]} ficheiro.md")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as ficheiro:
        markdown = ficheiro.read()

    print(markdown_to_html(markdown))