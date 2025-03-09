# ProyectoDiscretas1

# Documento explicativo 

Este programa es un evalua de fórmulas en lógica proposicional. Permite:
- Evaluar fórmulas con valores de verdad predefinidos para sus átomos (Parte A).
- Determinar si una fórmula es una **tautología**, **contradicción** o **contingencia** probando todas sus posibles valoraciones de verdad (Parte B).

## Funciones

## **cadena_a_lista(cadena: str, ignorar: set) -> list[str]**
Convierte una cadena en una lista de caracteres, eliminando los que están en el conjunto ignorar.

#### Parámetros:
- cadena: La cadena con la fórmula.
- ignorar: Conjunto de caracteres a eliminar (Espacios en blanco).

#### Return:
La lista de caracteres sin los elementos ignorados.

## **generar_valoraciones(atomos: list) -> list[dict]**
Genera todas las combinaciones posibles de valores de verdad para una lista de átomos.

#### Parametros:
- atomos: Lista de variables (átomos) presentes en una fórmula lógica.

#### Como funciona?
Calcula cuántos átomos hay y cuántas combinaciones posibles existen (2^N) a cada combinación le asigna valores de verdad (True o False) a los átomos, usa divisiones para alternar entre False y True de manera ordenada y poder crear todas las combinaciones posibles con los átomos dados. Devuelve una lista con todos los posibles valores de verdad para los átomos.

#### Return
Una lista de diccionarios, donde cada diccionario representa una combinación de valores de verdad para los átomos.


## **valorar_expresion(expresion: list, izq: int, der: int)**
Evalúa una expresión utilizando los valores de verdad almacenados.

#### Parametros:
- Expresion: Lista de caracteres que representa la fórmula lógica.
- izq: Índice inicial dentro de la expresión.
- der: Índice final dentro de la expresión.

#### Como funciona?
Si la expresión es un solo átomo, devuelve su valor de verdad almacenado, Sino empieza con !, devuelve la negación de la evaluación recursiva, Sino la expresión está entre paréntesis, busca el operador principal & o | y evalúa recursivamente ambos lados:
   - & (conjunción): True si ambos operandos son True.
   - | (disyunción): True si al menos uno de los operandos es True.

#### Print:
True o False según la evaluación, sino -1 si la expresión no es válida.


## **evaluar_formula(formula: str, atomos: list)**
Determina si una fórmula es una tautología, contradicción o contingencia.

#### Parametros:
- formula: La fórmula en formato de cadena.
- atomos: Lista de átomos que aparecen en la fórmula.

#### Como funciona?
Convierte la fórmula en una lista de caracteres sin espacios, con esta lista, genera todas las combinaciones de valores de verdad para los átomos, después, evalúa la fórmula con cada combinación y almacena los resultados. Por último clasifica la fórmula:
- 1 si es una tautología.
- 0 si es una contradicción.
- -1 si es una contingencia o si la fórmula es inválida.


## **main()**
Función principal que gestiona la entrada y salida.

#### Como funciona?
##### Parte A:
Lee el número de átomos (N) y sus valores de verdad, también, lee (M) fórmulas y las evalúa con los valores dados e imprime 1 si la fórmula es True, 0 si es False.

##### Parte B:
Lee S fórmulas y extrae los átomos presentes, las evalúa con todas las combinaciones posibles de valores de verdad e imprime 1 si es tautología, 0 si es contradicción, -1 si es contingencia.

## Ejemplo de Entrada y Salida

### Parte A:
#### Entrada:
- 2
- p 1
- q 0
- 3
- (p & q)
- (p | q)
- !(p & q)

#### Salida:
- 0
- 1
- 1

### Parte B:
#### Entrada:
- 2
- (p | !p)
- (p & !p)

#### :Salida:
- 1
- 0


