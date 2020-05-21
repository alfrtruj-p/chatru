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


def two_letters_syllable(fir_syl, y):  # make a syllable of two letters
    fir_syl[fir_syl.index(y):(fir_syl.index(y) + 2)] = [''.join(fir_syl[fir_syl.index(y):(fir_syl.index(y) + 2)])]


def three_letters_syllable(fir_syl, y):  # make a syllable of three letters
    fir_syl[fir_syl.index(y):(fir_syl.index(y) + 3)] = [''.join(fir_syl[fir_syl.index(y):(fir_syl.index(y) + 3)])]


def create_syllables(wor):  # creates the syllables, given a word in a dict/ removed - letters_in_wor
    print(wor)
    for x in wor:
        if x == 'a' or x == 'á':
            if wor.index(x) == 0:
                if len(wor) == 1:
                    pass
                else:
                    if wor == ['a', 'l']:
                        two_letters_syllable(wor, x)
                    elif wor == ['a', 'u', 'n']:
                        three_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'b' and wor[wor.index(x) + 2] == 's' \
                            and wor[wor.index(x) + 3] in ('t', 'c'):
                        three_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'd' and wor[wor.index(x) + 2] == 's' \
                            and wor[wor.index(x) + 3] == 'c':
                        three_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'h' and wor[wor.index(x) + 2] in ('i', 'u') \
                            and wor[wor.index(x) + 3] in ('y', 't'):
                        three_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'i' and wor[wor.index(x) + 2] in ('s', 'n') \
                            and wor[wor.index(x) + 3] in ('d', 'l'):
                        three_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'u' and wor[wor.index(x) + 2] in ('s', 'n') \
                            and wor[wor.index(x) + 3] in ('q', 't'):
                        three_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'b' and wor[wor.index(x) + 2] in ('d', 'j', 'n', 's'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'c' and wor[wor.index(x) + 2] in ('t', 'c'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'd' and wor[wor.index(x) + 2] in ('h', 'm', 'v'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'f' and wor[wor.index(x) + 2] == 'g':
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'i' and wor[wor.index(x) + 2] in ('r', 's'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'l' and \
                            wor[wor.index(x) + 2] in ('b', 'c', 'd', 'f', 'g', 'h', 'm', 'p', 'q', 'r', 't', 'z'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'm' and wor[wor.index(x) + 2] in ('b', 'p'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'n' and \
                            wor[wor.index(x) + 2] in ('c', 'd', 'f', 'g', 's', 't', 'v', 'z'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'r' and \
                            wor[wor.index(x) + 2] in ('b', 'c', 'd', 'g', 'm', 'p', 'q', 's', 't'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 's' and wor[wor.index(x) + 2] in ('c', 'f', 'm', 'n', 'p', 'q', 't'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'u':
                        two_letters_syllable(wor, x)
                    else:
                        first_vowel.append(x)
                        wor.remove(x)
            else:
                wor[(wor.index(x) - 1):(wor.index(x) + 1)] = [''.join(wor[(wor.index(x) - 1):(wor.index(x) + 1)])]
        elif x == 'e' or x == 'é':
            if wor.index(x) == 0:
                if len(wor) == 1:
                    break
                else:
                    if wor == ['e', 'l']:
                        two_letters_syllable(wor, x)
                    elif wor == ['e', 'n']:
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'm' and wor[wor.index(x) + 2] in ('b', 'p'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'n' and \
                            wor[wor.index(x) + 2] in ('c', 'd', 'f', 'g', 'j', 'l', 'r', 's', 't', 'v', 'y', 'z'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 's' and wor[wor.index(x) + 2] in ('b', 't'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'u':
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'x' and wor[wor.index(x) + 2] in ('c', 'h', 'p', 't'):
                        two_letters_syllable(wor, x)
                    else:
                        first_vowel.append(x)
                        wor.remove(x)
            else:
                wor[(wor.index(x) - 1):(wor.index(x) + 1)] = [''.join(wor[(wor.index(x) - 1):(wor.index(x) + 1)])]
        elif x == 'i' or x == 'í':
            if wor.index(x) == 0:
                if len(wor) == 1:
                    pass
                else:
                    if wor == ['i', 'r']:
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'm' and wor[wor.index(x) + 2] in ('b', 'p'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'n' and wor[wor.index(x) + 2] == 's' \
                            and wor[wor.index(x) + 3] in ('p', 't'):
                        three_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'n' and \
                            wor[wor.index(x) + 2] in ('c', 'd', 'f', 'g', 'h', 'j', 'm', 'n', 'q', 's', 't', 'v', 'y'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'r' and \
                            wor[wor.index(x) + 2] == 's':
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 's' and wor[wor.index(x) + 2] in ('l', 'r'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'z' and wor[wor.index(x) + 2] == 'q':
                        two_letters_syllable(wor, x)
                    else:
                        first_vowel.append(x)
                        wor.remove(x)
            else:
                wor[(wor.index(x) - 1):(wor.index(x) + 1)] = [''.join(wor[(wor.index(x) - 1):(wor.index(x) + 1)])]
        elif x == 'o' or x == 'ó':
            if wor.index(x) == 0:
                if len(wor) == 1:
                    pass
                else:
                    if wor == ['o', 's']:
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'e':
                        first_vowel.append(x)
                        wor.remove(x)
                    elif wor[wor.index(x) + 1] == 'b' and wor[wor.index(x) + 2] == 's' \
                            and wor[wor.index(x) + 3] in ('c', 't'):
                        three_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'b' and wor[wor.index(x) + 2] in ('c', 'j', 'n', 's', 't', 'v'):
                        two_letters_syllable(wor, x)
                    elif wor == ['o', 'i', 'r']:
                        three_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'i' and wor[wor.index(x) + 2] in ('d', 'g'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'l' and wor[wor.index(x) + 2] in ('m', 'v'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'm' and wor[wor.index(x) + 2] in ('b', 'n'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'n' and wor[wor.index(x) + 2] in ('c', 'd', 'z'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'p' and wor[wor.index(x) + 2] == 'c':
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'r' and \
                            wor[wor.index(x) + 2] in ('b', 'd', 'f', 'g', 'l', 'n', 'q', 't'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 's' and wor[wor.index(x) + 2] in ('c', 't'):
                        two_letters_syllable(wor, x)
                    else:
                        first_vowel.append(x)
                        wor.remove(x)
            else:
                wor[(wor.index(x) - 1):(wor.index(x) + 1)] = [''.join(wor[(wor.index(x) - 1):(wor.index(x) + 1)])]
        elif x == 'u' or x == 'ú':
            if wor.index(x) == 0:
                if len(wor) == 1:
                    pass
                else:
                    if wor == ['u', 'n']:
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'm' and wor[wor.index(x) + 2] == 'b':
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'n' and wor[wor.index(x) + 2] == 't':
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'l' and wor[wor.index(x) + 2] in ('c', 't'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 'r' and wor[wor.index(x) + 2] in ('b', 'd', 'g', 'n', 't'):
                        two_letters_syllable(wor, x)
                    elif wor[wor.index(x) + 1] == 's' and wor[wor.index(x) + 2] == 't':
                        two_letters_syllable(wor, x)
                    else:
                        first_vowel.append(x)
                        wor.remove(x)
            else:
                wor[(wor.index(x) - 1):(wor.index(x) + 1)] = [''.join(wor[(wor.index(x) - 1):(wor.index(x) + 1)])]
        """elif x == 'b':
            if wor[wor.index(x) + 1] == 'a' and wor[wor.index(x) + 2] in ('b', 'c', 'd', 'h', 'i', 'l', 'm',
                                                                          'n', 'p', 'r', 's', 'u', 'y'):
                three_letters_syllable(wor, x)"""
    print(first_vowel)
    print(wor)
    if first_vowel:
        wor.insert(0, first_vowel[0])
    print(wor)


def swap_syllables(palabra):  # x is a word value in a dict. The syllables in the word are swapped
    b = len(palabra)
    print(f"El numero de silabas en la palabra '{''.join(palabra)}' es: {b}")
    if b == 4 or b == 5:
        palabra[0], palabra[1] = palabra[1], palabra[0]
        palabra[2], palabra[3] = palabra[3], palabra[2]
    elif b == 2 or b == 3:
        palabra[0], palabra[1] = palabra[1], palabra[0]


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

    all_words = {}
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

    print(f'La traduccion en chutra es:{chutra_total}')
    print('')
    mas_traduccion = input(f'Quieres continuar traduciendo? (si/no): ')
    if mas_traduccion == 'no':
        otra_vez = False
m = input("Presiona una tecla para salir")
print('hello')

