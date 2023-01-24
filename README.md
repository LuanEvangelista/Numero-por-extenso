# Numero-por-extenso

A estrutura de dicionário "Banco_de_dados" é usada para armazenar palavras correspondentes a números de 1 a 900. Ele contém quatro chaves, "BOX1", "BOX2", "BOX3" e "BOX4", cada uma delas representa uma faixa de números. "BOX1" contém números de 1 a 10, "BOX2" contém números de 11 a 19, "BOX3" contém números de 20 a 90 com dezenas e "BOX4" contém números de 100 a 900 com centenas.

A função "unidade" lê uma entrada do usuário e verifica se é um número usando a função "isnumeric()". Se for, ele determina o tamanho do número. A partir daí, a função usa vários blocos de if-else para verificar o tamanho do número e o valor de cada dígito para imprimir a palavra correspondente.

Por exemplo, se o número de entrada for "11", a função verifica o tamanho do número, que é 2. Ele então verifica se o número é "11" e, se sim, ele usa o dicionário "Banco_de_dados" para encontrar a palavra correspondente a "11" na chave "BOX2", que é "onze". E imprime "onze".

De forma semelhante, se o número de entrada for "26", a função verifica o tamanho do número, que é 2. Ele então verifica se o primeiro digito é diferente de 1, e se sim, ele usa o dicionário "Banco_de_dados" para encontrar a palavra correspondente a "20" na chave "BOX3", que é "vinte" e usa o dicionário "Banco_de_dados" para encontrar a palavra correspondente a "6" na chave "BOX1", que é "seis". E imprime "vinte e seis".

É importante notar que o código não trata casos especiais como números acima de 900 ou menores que 1, ou casos em que o número não é numérico.

![1](https://user-images.githubusercontent.com/82175827/144888557-b89e8701-3cbd-4ca0-a846-bc2435767233.PNG)
