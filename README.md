IMPORTANTE: Consideraciones relevantes sobre las prácticas

En este documento hacemos algunas consideramos que consideramos relevantes de cara a mejorar la calidad de las prácticas que faltan por realizar lo cual redundará en una mejor calificación.

- Es importante asegurarse de que el **pdf** en el que describimos el trabajo realizado esté bien escrito, bien organizado y que contenga todo lo que se nos pide, adecuadamente explicado y documentado. Por ejemplo:
  - "el programa hace todo lo que se pide" es una frase que no aporta nada y por tanto *no es una breve descripción de las ampliaciones realizadas.*
  - "los resultados son los esperados" tampoco aporta nada y por tanto no es *un análisis crítico de los resultados.*

- **Es importante organizar el código en funciones**:
  - Cada función debe agrupar aquellas instrucciones que tengan un único fin y que pueden ser ejecutadas independientemente de otras porciones de código.
  - En un programa debe evitarse tanto como sea posible la existencia de líneas fuera de una función, salvo para cosas específicas como realizar la llamada a la función principal que pone en marcha lo que se espere que realice el programa. 

- Es fundamental utilizar **nombres significativos para clases, métodos, funciones, variables y constantes**. El código tiene que poder leerse como si fuera un libro. No debemos usar nombres como Clase1, metodoA, o x en lugar de Queue, enqueue o maximo\_valor que dan significado al dato que representan. Así, a cualquiera que lea nuestro código (incluidos nosotros mismos) le será más fácil comprenderlo.

- **Hay que evitar la repetición de código**. Para ello hay que pensar en:
  - **Parametrizar** el código. Por ejemplo, un trozo de código como este:
  - `		`if n==1:
    - `		`resultado = algo\*1
  - `		`elif n==2:
    - `		`resultado = algo\*2
  - `		`elif n==3:
    - `		`resultado = algo\*3

`		`se puede reemplazar por llamadas a una función

`		`def miFuncion(algo, n):

`		`return algo\*n

- **Agrupar** estructuras de datos elementales:

`		`En lugar definir cosaA, cosaB, cosaC, ..., cosaX y repetir n veces el código que realiza las manipulaciones de cada "cosa", podemos agrupar todas las "cosas" en una lista de "cosas" y utilizar bucles del tipo:

`		`for i in range :

`		`cosa = listaDeCosas[i]       # obtengo una cosa de la lista de cosas

`		`código para manipular "cosa" # manipulo "cosa"

`		`listaDeCosas[i] = cosa       # almaceno la "cosa" resultante en la lista (si es necesario)

- Debemos **documentar adecuadamente el código.** Es relativament frecuente que os olvidéis de los docstrings:
  - Cada módulo, clase, función, etc, debe tener su *docstring.*
  - Un *docstring* es un string, un #comentario después de la cabecera de una función no sirve como *docstring* 

- Debemos **analizar críticamente** el código y el resultado de las ejecuciones. Por ejemplo:
  - Si observamos que se produce un error para ciertos casos, hay que pensar si sería posible detectar y corregir ese error o al menos informar mediante una excepción de que se da esa situación.
  - Si al incrementar el número de simulaciones los resultados no convergen a los esperados, puede ocurrir que:
    - la teoría de probabilidades es errónea
    - la impementación de nuestro modelo es errónea

La causa 1 parece improbable, estamos trabajando con algo que no se inventó ayer y lleva siendo aplicado con éxito algún tiempo, por lo que probablemente la causa sea la 2. ¿Tal vez estamos realizando todas las simulaciones con los mismos datos?
