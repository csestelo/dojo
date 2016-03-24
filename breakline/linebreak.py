def linebreak(text, columns):
    if text == '':
        return text
    if len(text) - columns == 1 and text[-1] == ' ':
        text = text[:-1]
        return text
    else:
        return text[:columns] + '\n' + text[columns:]


def linebreak2(text, columns):
    lines = []
    while text:
        pos = 0
        last_space = None
        broken = False
        for letter in text:
            if letter == ' ':
                last_space = pos
            if pos == columns and last_space is not None:
                lines.append(text[:last_space])
                broken = True
                break
            pos += 1
        else:
            if len(text) > columns:
                raise ValueError('Can\'t break word: "{}"'.format(text))
            lines.append(text)
        update_idx = last_space if broken else pos
        text = text[update_idx + 1:]
    return '\n'.join(lines)


def linebreak3(text, columns):
    lines = []
    # enquanto text nao eh vazio, i.e. text != ''
    # lembre que coisas vazias em python sao consideradas falsas
    while text:
        last_space = None
        # enumerate retorna tuplas (posicao, elemento)
        for pos, letter in enumerate(text):
            if letter == ' ':
                last_space = pos
            # quando chegamos ao limite. note que no corpo desse if assumimos
            # que ja vimos um espaco antes (o texto eh quebravel), entao a gente
            # precisa garantir que o last_space nao eh None (vide o else do for)
            if pos == columns and last_space is not None:
                # fazemos as alteracoes baseadas no ultimo espaco
                update_idx = last_space
                break  # para o for no meio
        # soh entra no else quando o for chega ao final, i.e. nao deu break,
        # i.e. a ultima linha eh menor que o limite de colunas
        else:
            # o caso em que a palavra eh maior que o limite
            if len(text) > columns:
                raise ValueError('Can\'t break word: "{}"'.format(text))
            # fazemos as alteracoes baseadas na pos. o + 1 eh porque no slice o
            # limite final nao eh icluso, entao tem que adicionar 1 para incluir
            # a string at o final
            update_idx = pos + 1
        curr_line = text[:update_idx]
        rest_of_text = text[update_idx + 1:]
        lines.append(curr_line)
        text = rest_of_text
    return '\n'.join(lines)


def linebreak3_2(text, columns):
    lines = []
    while text:
        last_space = None
        for pos, letter in enumerate(text):
            if letter == ' ':
                last_space = pos
            if pos == columns and last_space is not None:
                update_idx = last_space
                break
        else:
            if len(text) > columns:
                raise ValueError('Can\'t break word: "{}"'.format(text))
            update_idx = pos + 1
        curr_line = text[:update_idx]
        rest_of_text = text[update_idx + 1:]
        lines.append(curr_line)
        text = rest_of_text
    return '\n'.join(lines)
