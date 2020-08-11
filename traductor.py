from silabas import silabas


def split_words(letters_in_sentence, number_words_in_sentence,
                words_in_dict):  # split the words from a list and assign them as values to a dict
    j = 0
    i = 0
    k = 1
    words = []
    while j <= number_words_in_sentence:
        while letters_in_sentence[i] != ' ':
            words.append(letters_in_sentence[i])
            if i == len(letters_in_sentence) - 1:
                break
            i += 1
        words_in_dict.update({('palabra_' + str(k)): words})
        words = []
        del letters_in_sentence[0:i + 1]
        k += 1
        i = 0
        j += 1


def swap_syllables(silabas):  # x is a word value in a dict. The syllables in the word are swapped
    b = len(silabas)
    print(f"El numero de silabas en la palabra '{''.join(silabas)}' es: {b}")
    if b == 4 or b == 5:
        silabas[0], silabas[1] = silabas[1], silabas[0]
        silabas[2], silabas[3] = silabas[3], silabas[2]
    elif b == 2 or b == 3:
        silabas[0], silabas[1] = silabas[1], silabas[0]
    return silabas


otra_vez = True
while otra_vez:
    text = input(f'Escribe lo que deseas traducir: ')
    while text == '':
        repeat = input(f'No escribiste nada, escribe otra vez: ')
        text = repeat
    letters = list(text)
    number_of_words = letters.count(' ')
    # print(f'El numero de palabras es: {number_of_words + 1}')
    # print(f'El numero de letras es: {len(letters)}')

    palabra_en_chutra = swap_syllables(silabas(text))
    print(f'La traduccion en chutra es:{palabra_en_chutra}')

    """all_words = {}
    split_words(letters, number_of_words, all_words)

    first_vowel = []
    chutra_total = ''
    for v in all_words.keys():
        word = all_words[v]
        create_syllables(word)
        swap_syllables(word)
        chutra = ''.join(word)
        chutra_total = chutra_total + ' ' + chutra
        first_vowel = []

    print(f'La traduccion en chutra es:{chutra_total}')"""
    print('')
    mas_traduccion = input(f'Quieres continuar traduciendo? (si/no): ')
    if mas_traduccion == 'no':
        otra_vez = False
m = input("Presiona una tecla para salir")


