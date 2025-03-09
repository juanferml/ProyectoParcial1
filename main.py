from sys import stdin

valores = dict()

# Pasa de str a lista
def cadena_a_lista(cadena: str, ignorar: set) -> list[str]:
    return [caracter for caracter in cadena if caracter not in ignorar]
  
# Genera las combinaciones de los valores de verdad para los átomos
def generar_valoraciones(atomos):
    cantidadAtomos = len(atomos)
    total_combinaciones = 2 ** cantidadAtomos
    valoraciones = []
    
    for i in range(total_combinaciones):
        combinacion = {}
        divisor = total_combinaciones // 2
        for j in range(cantidadAtomos):
            if (i // divisor) % 2 == 0:
                combinacion[atomos[j]] = False
            else:
                combinacion[atomos[j]] = True
            divisor //= 2
        valoraciones.append(combinacion)
    return valoraciones


# Evalúa una expresión lógica utilizando los valores de verdad dados
def valorar_expresion(expresion: list, valores_verdad: dict, izq: int, der: int):
    resultado = -1
    if izq == der:
        return valores_verdad.get(expresion[izq], -1)  # Devuelve -1 si el átomo no está definido
    elif expresion[izq] == '!':
        resultado = valorar_expresion(expresion, valores_verdad, izq + 1, der)
        return -1 if resultado == -1 else (0 if resultado else 1)
    elif expresion[izq] == '(' and expresion[der] == ')':
        contador_parentesis = 0
        i, operador_medio = izq + 1, -1
        while i < der and operador_medio == -1:
            if expresion[i] == '(':
                contador_parentesis += 1
            elif expresion[i] == ')':
                contador_parentesis -= 1
            if expresion[i] in {'&', '|'} and contador_parentesis == 0:
                operador_medio = i
            i += 1

        if operador_medio == -1:
            return -1  # Expresión inválida

        izquierda = valorar_expresion(expresion, valores_verdad, izq + 1, operador_medio - 1)
        derecha = valorar_expresion(expresion, valores_verdad, operador_medio + 1, der - 1)

        if expresion[operador_medio] == '&':
            resultado = izquierda and derecha
            if resultado == True:
                resultado = 1
            elif resultado == False:
                resultado = 0    
        elif expresion[operador_medio] == '|':
            resultado = izquierda or derecha
            if resultado == True:
                resultado = 1
            elif resultado == False:
                resultado == 0

    return resultado  # Si no cumple ninguna condición válida, es una expresión inválida


# Determina si una fórmula es tautología, contradicción o contingencia
def evaluar_formula(formula: str, atomos: list):
    expresion = cadena_a_lista(formula, {' '})
    valoraciones_posibles = generar_valoraciones(atomos)
    resultados = set()
    
    for valores_verdad in valoraciones_posibles:
        resultado = valorar_expresion(expresion, valores_verdad, 0, len(expresion) - 1)
        if resultado == -1:
            return -1  # Expresión inválida
        resultados.add(resultado)
    
    if len(resultados) == 1:
        return 1 if True in resultados else 0  # Tautología o contradicción
    return -1  # Contingencia

def main():
    # Parte A:
    N = int(stdin.readline().strip())
    valores_verdad = {}
    for i in range(N):
        variable, valor = stdin.readline().split()
        valores_verdad[variable] = bool(int(valor))
    
    M = int(stdin.readline().strip())
    for i in range(M):
        formula = cadena_a_lista(stdin.readline().strip(), {' '})
        resultado = valorar_expresion(formula, valores_verdad, 0, len(formula) - 1)
        print(resultado)
    
    # Parte B:
    S = int(stdin.readline().strip())
    for i in range(S):
        formula = stdin.readline().strip()
        atomos = sorted(set(caracter for caracter in formula if caracter.isalpha()))
        resultado = evaluar_formula(formula, atomos)
        print(resultado)

main()