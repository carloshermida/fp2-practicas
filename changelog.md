### Changelog

---

###### 13/09/22
####  Readme y Changelog - _last commit_
* Implementación del readme para resumir el contenido del repositorio
* Utilización de este changelog para explicar los cambios realizados

---

###### 21/05/21
#### (P4) random_people v4.0.0 - [0b0fbbb](https://github.com/carloshermida/fp2-practicas/commit/0b0fbbb53f37c2ba86dec644599d2fab9ed17808)
* Se mejora random_people al tener en cuenta de que ahora consideramos que los socios mayores de edad podrán tener varios menores de edad abonados bajo su DNI. 
* Se generarán aleatoriamente menores de edad con una probabilidad menor de 0.25 para los socios. Para poder distinguirlos a la hora de generar la lista les añadimos delante del dni un $ que indica que este socio tendrá abonados y estes estarán situados en las líneas inferiores señalados con un @
* Se crea la función prices que calculará el precio a pagar en función de la ubicación y el numero de sus abonados
* Se habilita la posibilidad de poder fusionar un número de equipos arbitrario

---

###### 21/05/21
#### (P4) main v4.0.0 - [00f9d6b](https://github.com/carloshermida/fp2-practicas/commit/00f9d6b99229bdd28a3c19c248a58b0ed8648790)
* Se le añade al módulo principal nuevas funciones
* Se crea la función forest capaz de convertir los ficheros de texto en árboles
* Se crea la función grafting capaz de unificar 2 árbol en uno solo
* Preorder_indent_BST se emplea para ir mostrando el contenido de los árboles
* Chop_down transforma un árbol a fichero de texto

---

###### 20/05/21
#### (P4) partner v1.0.0 - [26a0717](https://github.com/carloshermida/fp2-practicas/commit/26a0717c4ed5f32387660837c1b6f8259b4c3d02)
* Creación del módulo Partner donde se define la clase socio a la que se dota de
dni, nombre, fecha de nacimiento y ubicación

---

###### 20/05/21
#### (P4) rp v1.0.1 - [9faa117](https://github.com/carloshermida/fp2-practicas/commit/9faa117a31b288e9a75ef54745240b53b10c669d)
* Creación del módulo random_people.py con las funciones para aportar a cada persona un DNI, apellidos y nombre y fecha de nacimiento.

---

###### 20/05/21
#### (P4) avlt v1.0.0 - [3f5216f](https://github.com/carloshermida/fp2-practicas/commit/3f5216ff7896ccf5c524d2f68788168c2589ed14)
* Importamos todos los módulos pertinentes aportados para el correcto
funcionamiento de los árboles con los que posteriormente trabajaremos

---

###### 08/05/21
#### (P3) main v4.0.0 - [2929c62](https://github.com/carloshermida/fp2-practicas/commit/2929c62172789998b9e711e993f5cfb6aa60c00e)
* Mejora de la selección de países, añadiendo la opción de utilizar la distribución real. Se crea un grupo reducido de paises, “BigFive”, que serán constantes en todos los concursos, al igual que sucede en la realidad

---

###### 08/05/21
#### (P3) ballot v4.0.0 - [899dde0](https://github.com/carloshermida/fp2-practicas/commit/899dde0281f859f0e22ad82b54ca494eed571725)
* Mejora del funcionamiento de la función de votación
* Implementación del ranking. Si la lista estaba vacía se añade de primero. Si no
estaba el país se compararán sus puntos con los de los que ya se encuentran ahí y se insertará inmediatamente antes del primer elemento que encuentre, a medida que la vaya recorriendo la lista, con una puntuación menor que él. En el caso de que ya estuviera, se le volverá a insertar con la nueva puntuación y se eliminará el anterior

---

###### 05/05/21
#### (P3) ballot v1.0.0 - [aef149d](https://github.com/carloshermida/fp2-practicas/commit/aef149d94449b947775e92b8bdad127f99ae37b5)
* Creación de la función votación que mediante bucles recorrerá los países de la
lista barajada. Para cada uno creará otra lista sin el país que va a votar y de esta se extraerán aleatoriamente los afortuandos a los cuales les tocaron puntos. Se almacenarán los puntos que van acumulando los países mediante la función setPuntos

---

###### 04/05/21
#### (P3) countries v0.0.1 - [7a0e621](https://github.com/carloshermida/fp2-practicas/commit/7a0e621038100e2bf134b55ac9b1004e54f138c7)
* Creación de las funciones de la clase Countries
* Adición de los módulos Array_positional_list , Linked_positional_list y Doubly_linked_base para poder trabajar después con las listas posicionales

---

###### 04/05/21
#### (P3) main v0.0.1 - [ee2fdbb](https://github.com/carloshermida/fp2-practicas/commit/ee2fdbb6b9ab2fff13b5455249df9113347c7d86)
* Creación del módulo principal con las funciones encargadas de crear la lista de participantes.

---

###### 18/04/21
#### (P2) categories v4.0.0 - [71b6dc1](https://github.com/carloshermida/fp2-practicas/commit/71b6dc1de496add32e0d271616282461ac8e0e3a)
* Creación de un nuevo módulo Categories con clase para vacunas, mejorando así
su adición

---

###### 18/04/21
#### (P2) stockist v4.0.0 - [28d87fc](https://github.com/carloshermida/fp2-practicas/commit/28d87fcfe4765c538cbb76d3a2278d5a01ec17fd)
* Creación del módulo stockist donde se sitúan funciones para gestionar la
distribución de vacunas y listas de espera
* Implementación de la función que mostrará los datos resultantes de las
vacunaciones diarios y totales

---

###### 18/04/21
#### (P2) sample v4.0.0 - [d28feda](https://github.com/carloshermida/fp2-practicas/commit/d28fedafeb900a178ca440bf43cf6fec3fa690ba)
* Creación del módulo sample para agrupar las funciones relacionadas con la selección de edades gallegas y la implementación de estas

---

###### 18/04/21
#### (P2) add v4.0.0 - [3d15b51](https://github.com/carloshermida/fp2-practicas/commit/3d15b51cda302a622d35eeaf4a6568c6828d506b)
* Creación del módulo add donde se recogen las funciones para añadir las vacunas y personas

---

###### 18/04/21
#### (P2) main v3.0.0 - [7b7b5a6](https://github.com/carloshermida/fp2-practicas/commit/7b7b5a67168af6ca87f6526495a05d2639368d02)
* Creación del módulo principal con las funciones encargadas de crear las colas
necesarias
* Creación de las funciones capaces de leer los argumentos apartados por el
usuario y trabajar con las colas

---

###### 08/04/21
#### (P2) array_queue v0.0.1 - [43f3f68](https://github.com/carloshermida/fp2-practicas/commit/43f3f68aaf907aff8abc8f466be81593b414ca2d)
* Creación de las funciones de la clase Colas

---

###### 29/03/21
#### (P1) main v4.0.0 - [082ca31](https://github.com/carloshermida/fp2-practicas/commit/082ca31a761feaf0f2a0153406162facb4469db1)
* Creación del manual de usuario y del menú principal

---

###### 28/03/21
#### (P1) writtingcheck v2.2.0 - [edbe453](https://github.com/carloshermida/fp2-practicas/commit/edbe4537074620c904846dbc44cb6a9b94f8ead8)
* Creación del módulo writingcheck, encargado de verificar que el infijo
introducido por el usuario está correctamente escrito
* Implementación de la función espaciador, que facilita la escritura al usuario,
añadiendo espacios donde sea necesario
* Contemplación de más errores derivados del uso incorrecto del programa

---

###### 28/03/21
#### (P1) calculus v2.2.0 - [a7c6a5c](https://github.com/carloshermida/fp2-practicas/commit/a7c6a5c549bc5462ba00f0c17469c404b3b7128c)
* Creación de la función iniciar, la cual analiza el postfijo en busca de operadores
y se apoya en la función operador para realizar el cálculo correcto
* Implementación de la función operador_especial, que añade funciones trigonométricas y raíces cuadradas

---

###### 28/03/21
#### (P1) itp v2.2.0 - [575c642](https://github.com/carloshermida/fp2-practicas/commit/575c64267e91b05dd8a1c11c8745dbf588cd74da)
* Implementación de la función infixtoPostfix, que convierte una expresión infija a
postfija

---

###### 25/03/21
#### (P1) stack v1.0.0 - [b012a3a](https://github.com/carloshermida/fp2-practicas/commit/b012a3a2cb16783059b9cc4d110ca01f835a95e4)
* Creación de las funciones de la clase Pila
