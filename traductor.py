from silabas import silabas


def separar_palabras(texto): # separa las palabras del texto en una lista
    palabras = texto.split()
    return palabras


def palabras_en_chatru(palabra): # toma cada una de las palabras y las traduce a chatru en una lista
    texto_en_chatru = []
    for x in palabra:
        silabas_separadas = silabas(x)
        palabra_en_chatru = trocar(silabas_separadas)
        texto_en_chatru.append(palabra_en_chatru)
    return texto_en_chatru


def trocar(palabra):
    puntuacion = ''
    if palabra[-1] in (',', '.', ';', ':', '?'):  # quitar la puntuación al final de una palabra
        puntuacion = palabra[-1]
        palabra = palabra[0:-1]
    b = len(palabra)
    if b == 6 or b == 7:
        palabra[0], palabra[1] = palabra[1], palabra[0]
        palabra[2], palabra[3] = palabra[3], palabra[2]
        palabra[4], palabra[5] = palabra[5], palabra[4]
    if b == 4 or b == 5:
        palabra[0], palabra[1] = palabra[1], palabra[0]
        palabra[2], palabra[3] = palabra[3], palabra[2]
    elif b == 2 or b == 3:
        palabra[0], palabra[1] = palabra[1], palabra[0]
    if puntuacion != '':
        palabra.append(puntuacion)
    silabas_trocadas = ''.join(palabra)
    return silabas_trocadas


while True:
    texto = input(f'Escribe lo que deseas traducir del español: ')
    while texto == '':
        repeat = input(f'No escribiste nada, escribe otra vez: ')
        texto = repeat
    palabras = separar_palabras(texto)
    chatru = palabras_en_chatru(palabras)
    texto_en_chatru = ' '.join(chatru)
    print('')
    print(f'La traducción en chutra es: {texto_en_chatru}')
    print('')
    mas_traduccion = input(f'Quieres continuar traduciendo? (si/no): ')
    if mas_traduccion != 'si':
        break
m = input("Presiona una tecla para salir")


