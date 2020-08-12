# http://elies.rediris.es/elies4/Fon2.htm
# http://liceu.uab.es/~joaquim/general_linguistics/gen_ling/fonologia/silaba/silaba.html


def silabas(palabra_a_traducir):
    silabas_en_la_palabra = []
    letra = 0

    palabra = minusculas(palabra_a_traducir)
    if palabra == 'numeros': # si hay un número en la palabra, no se traduce.
        silabas_en_la_palabra.append(palabra_a_traducir)
    else:
        while True:
            try:
                if letra >= len(palabra):
                    break
                salto = 0

                if consonante(palabra[letra]):
                    if guegui(palabra[letra + salto:]):  # esto es una chapu, pero no tengo otra forma por ahora :(
                        salto += 2
                    elif ataque_complejo(palabra[letra:letra + 2]):
                        salto += 2
                    else:
                        salto += 1

                else:
                    salto += 0  # vocal

                if triptongo(palabra[letra + salto:]):
                    salto += 3
                elif diptongo_con_h(palabra[letra + salto:]):
                    salto += 3
                elif diptongo(palabra[letra + salto:]):
                    salto += 2
                elif dieresis(palabra[letra + salto:]):
                    salto += 2
                else:
                    salto += 1

                salto += coda(palabra[letra + salto:])

                silaba = palabra[letra:letra + salto]
                letra += salto

                silabas_en_la_palabra.append(silaba)

            except IndexError:
                break

    return silabas_en_la_palabra


def vocal(letra):
    return True if letra in ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ü'] else False


def consonante(letra):
    return not vocal(letra)


def ataque_complejo(c):
    if len(c) < 2: return False
    return True if (c[0] in ['b', 'c', 'f', 'g', 'p', 't'] and c[1] in ['l', 'r'] and c != "dl") or c in [
        'dr', 'kr', 'll', 'rr', 'ch'] else False


def guegui(c):
    if len(c) < 3: return False
    return True if (c[0:1] == 'g' and c[1] == 'u' and c[2] in ['e', 'i']) else False


def diptongo(trozo):
    if len(trozo) < 2: return False
    if trozo[0:2] in ['ai', 'au', 'ei', 'eu', 'io', 'ou', 'ia', 'ua', 'ie', 'ue', 'oi', 'uo', 'ui',
                      'iu']: return True
    if len(trozo) == 2 and trozo in ['ay', 'ey', 'oy']: return True
    return False


def dieresis(trozo):
    if len(trozo) < 2: return False
    return True if trozo[0:2] in ['üe', 'üi'] else False


def diptongo_con_h(trozo):
    if len(trozo) < 3: return False
    t = trozo[0:3]

    if t[1] == 'h':
        if len(trozo) > 3 and trozo[2:4] == 'ue':
            return False
        else:
            t = t.replace('h', '')
    else:
        return False

    return diptongo(t)


def triptongo(trozo):
    if len(trozo) < 3: return False
    return True if trozo[0:3] in ['iai', 'iei', 'uai', 'uei', 'uau', 'iau', 'iái', 'iéi', 'uái', 'uéi',
                                  'uáu', 'iáu', 'uay', 'uey'] and len(trozo[3:]) < 2 else False


def coda(trozo):
    l = len(trozo)
    if l < 1: return 0  # fin de palabra, no quedan letras
    if l < 2 and consonante(trozo[0]): return 1  # V+C fin de palabra, se añade
    if l > 1 and ataque_complejo(trozo[0:2]): return 0  # V +C+C inseparables, a la siguiente
    if l > 1 and consonante(trozo[0]) and vocal([1]): return 0  # V +C+V, irá con la siguiente sílaba
    if l > 2 and consonante(trozo[0]) and consonante(trozo[1]) and vocal(trozo[2]): return 1  # V+C +C+V
    if l > 3 and consonante(trozo[0]) and ataque_complejo(trozo[1:3]) and vocal(trozo[3]): return 1  # V+C +C+C+V
    if l > 3 and consonante(trozo[0]) and consonante(trozo[1]) and consonante(trozo[2]) and vocal(
            trozo[3]): return 2  # V+C+C +C+V
    if l > 3 and consonante(trozo[0]) and consonante(trozo[1]) and consonante(trozo[2]) and consonante(
            trozo[3]): return 2  # V+C+C +C+C+V
    return 0


def minusculas(texto):
    contains_digit = any(map(str.isdigit, texto))
    if contains_digit:
        ret = 'numeros'
    else:
        ret = ""
        mapeo = {'Á': 'á', 'É': 'é', 'Í': 'í', 'Ó': 'ó', 'Ú': 'ú', 'Ü': 'ü', 'Ñ': 'ñ'}
        for letra in texto:
            if letra in mapeo:
                ret += letra.replace(letra, mapeo[letra])
            else:
                ret += letra.lower()
    return ret
