# As expressões regulares são importantes para sempre quando você precisa determinar padrões de textos, encontrar padrões em strings, as regex facilitam, como por exemplo variações da mesma palavra, como por exemplo palavras escritas de forma incorreta

# Roteiro

* O que é
* História
* Padrões
* Caracteres
* Exemplos
* Python + regex


#### O que são expressões regulares?

* Método formal de especificar um padrão de Texto |
  * São padroes para descrever string
* Notação para representar padrões em strings
* Composição de simbolos, caracteres e funções especiais, que, agrupados com caracteres formam uma expressão
  * metacaracteres que formam patterns de texto que especificam como uma string deve ser

#### História

* 1943: Funcionamento dos neorônios
  * Uma galera da neuciencia começou uma pesquisa para saber como funciona os neurônios e com reconhecimento de padrões neurologicos, eles chegaram num sistema que temos como base na regex
* 1968: no qed -> ed -> grep
  * qed um dos prim eiros editores com um campo de busca como um ctrl+f
  * ed um dos primeiros editores do unix
  * grep global regular expression pattern
    * ls -l | grep ago -> mostra os documentos que tem em agosto
* 1986: Regex (Clang) -> "ce-lang"


USE: `https://regexpal.com` [Regex Tester - Javascript, PCRE, PHP](https://www.regexpal.com/)

#### Caracteres [0]

| META / CARACTERES ESPECIAIS | FAZ O QUE?                    |                                                                                                                                                                                                                                                                          |
| --------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .                           | Qualquer caractere            | ![1674139757260](image/expressoesregulares/1674139757260.png)<br />![1674139815968](image/expressoesregulares/1674139815968.png)<br />Isso que define um pattern                                                                                                             |
| []                          | lista de caracteres           | ![1674139908946](image/expressoesregulares/1674139908946.png)<br />Recupera inclusive caracteres repetidos                                                                                                                                                                 |
| ?                           | anterior pode existir ou não | Usado caso a palavra esteja escrito errado,<br />por exemplo, pode ser que o caractere exista<br />ou pode ser que também não exista<br />![1674140203817](image/expressoesregulares/1674140203817.png)<br />![1674140412565](image/expressoesregulares/1674140412565.png) |
| .*                          | qualquer coisa                | ![1674141157282](image/expressoesregulares/1674141157282.png)                                                                                                                                                                                                              |
| {x}                         | anterior aparece x vezes      | ![1674141184576](image/expressoesregulares/1674141184576.png)                                                                                                                                                                                                              |
| $                           | Fim da linha                  | ![1674141237090](image/expressoesregulares/1674141237090.png)<br />Qualquer coisa que aparece no final do texto                                                                                                                                                            |
| +                           | Anterior ao menos uma vez     | ![1674140614396](image/expressoesregulares/1674140614396.png)<br />![1674140634803](image/expressoesregulares/1674140634803.png)                                                                                                                                             |
| (xy)                        | Cria grupos                   | ![1674140890858](image/expressoesregulares/1674140890858.png)                                                                                                                                                                                                              |
| ^                           | Começo da linha              | ![1674140918096](image/expressoesregulares/1674140918096.png)<br />Só pegou o primeiro porque é o único na primeira linha                                                                                                                                               |
| \                           | Escapa o meta                 | ![1674141119862](image/expressoesregulares/1674141119862.png)                                                                                                                                                                                                              |
| pipe                        | OU                            |                                                                                                                                                                                                                                                                          |
| [^]                         | Lista negada                  |                                                                                                                                                                                                                                                                          |
|                             |                               |                                                                                                                                                                                                                                                                          |
|                             |                               |                                                                                                                                                                                                                                                                          |
|                             |                               |                                                                                                                                                                                                                                                                          |
|                             |                               |                                                                                                                                                                                                                                                                          |


Exemplo:

![1674141409993](image/expressoesregulares/1674141409993.png)


#### Listas

Existem padrões posix

| META         | O QUE FAZ                       | EXEMPLO                                                     |
| ------------ | ------------------------------- | ----------------------------------------------------------- |
| [0-9]PIPE\d  | Acha todos os números          | ![1674141569128](image/expressoesregulares/1674141569128.png) |
| [a-z]        | acha todas as letras minusculas | ![1674145308164](image/expressoesregulares/1674145308164.png) |
| [^0-9]pipe\D | Acha tudo que não seja número | ![1674145412246](image/expressoesregulares/1674145412246.png) |
| \W           | Acha tudo se não seja letra    | ![1674145453657](image/expressoesregulares/1674145453657.png) |

Match não individual ![1674145807022](image/expressoesregulares/1674145807022.png)

| col1 | col2                            | col3                                                        |                                                                                                                            |
| ---- | ------------------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
|      | Recuperar um numero de telefone | ![1674146017110](image/expressoesregulares/1674146017110.png) | Pega o 9 no inicio se existir, pega de 0 até<br />9 que tenham 4 ocorrencias depois um traço<br />depois do 0 ao 9 que  |
|      |                                 |                                                             |                                                                                                                            |

#### Python + Regex = re

* Objetos
  * Um catadão de funções e constantes
* Métodos
  * objetos com regex compiladas e que apresentam alguns métodos

![1674146513938](image/expressoesregulares/1674146513938.png)

##### Objetos

* Compile
  * Compila uma expressão e a aplica a várias strings
    * Posso armazenar o padrão em uma var e buscar o padrão em muitas strings. Vai compilar a expressão, e a cada string que quiser compilar isso, ele vai funcionar ![1674146765779](image/expressoesregulares/1674146765779.png)
* Search
  * Procura uma expressão em qualquer posição de uma string
    * Como um operador de in ![1674146878667](image/expressoesregulares/1674146878667.png)
    * ![1674146966104](image/expressoesregulares/1674146966104.png)
    * Span mostra que está na posição 1 até a 2 na string
* Match[0] / Fullmatch[1]
  * Procura por uma expressão no inicio de uma string (startswith)
    * ![1674147178391](image/expressoesregulares/1674147178391.png)
  * Procura uma expressão exatamente igual
    * ![1674147236716](image/expressoesregulares/1674147236716.png)
* Split
  * Dada uma expressão, fatia os dados (divide os dados)
    * Split do python
      * ![1674147319076](image/expressoesregulares/1674147319076.png)
    * com re.split
      * ![1674147398797](image/expressoesregulares/1674147398797.png)
      * ![1674147439646](image/expressoesregulares/1674147439646.png)

##### Objetos [1]

* Findall

  * Retorna uma lista com todos os matchs encontrados
    * ![1674147582649](image/expressoesregulares/1674147582649.png)
    * ![1674147603978](image/expressoesregulares/1674147603978.png)
    * ![1674147649833](image/expressoesregulares/1674147649833.png)
* Finditer

  * Retorna um gerador com todos os matchs, cada um sendo um novo objeto de match

##### Métodos

* search
* match
* fullmatch
* findall / finditer
* **groups**
* **pattern**

![1674147937284](image/expressoesregulares/1674147937284.png)







### Exemplos:

* Pegando várias palavras:
  * ![1674148196146](image/expressoesregulares/1674148196146.png)
  *
