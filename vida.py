""" Define funções para criar e iterar autómatos celulares.
Na versão actual, está implementado o Jogo da Vida, de Conway, incluindo
algumas variantes não-standard do mesmo. """

def celula_vive(submatriz, regra = (3, 2, 3)):
    """ Determina se uma célula vive na geração seguinte

    submatriz é uma matriz quadrada com 9 elementos, onde o elemento central é
    a célula cuja vida é determinada de acordo com a regra escolhida.
    1 denota uma célula viva, 0 denota uma célula morta.
    Seja regra = (max_vizinhos, min_vizinhos, vizinhos_para_nascer).
    Uma célula viva:
      -- morre se tiver mais de max_vizinhos vivos;
      -- morre se tiver menos de min_vizinhos vivos;
      -- permanece viva nos restantes casos.
    Uma célula morta:
      -- renasce se tiver exactamente vizinhos_para_nascer vizinhos vivos;
      -- permanece morta nos restantes casos.
    Requires:
      submatriz é uma matriz 3x3 de 0s e 1s, formatada como uma lista
        de 3 listas, cada uma com 3 elementos; 
      regra é um triplo de int em que cada int está entre 0 e 8 inclusive.
    Ensures:
      True se a célula central fica viva com a regra escolhida,
        False caso contrário.
    """
    pass # código a completar pelos alunos

def cria_mundo(linhas, colunas):
    """ Cria um novo mundo com todas as células mortas

    Requires: linhas e colunas são int, cada um maior ou igual a 2.
    Ensures: uma matriz de 0s com as dimensões indicadas; a matriz é uma lista
      de listas, em que cada lista interna tem número de elementos dado por
      colunas, e a lista externa tem número de elementos dado por linhas.
    """
    pass # código a completar pelos alunos

def tamanho_mundo(mundo):
    """ Devolve o tamanho de um mundo

    Requires: mundo é uma matriz de 0s e 1s formatada como descrito no contrato
      de cria_mundo, com pelo menos 2 linhas e 2 colunas.
    Ensures: um par de int (linhas, colunas) correspondente às dimensões do
      mundo.
    """
    pass # código a completar pelos alunos

def atribui_valor_celula(mundo, linha, coluna, valor):
    """ Atribui um valor a uma célula

    Força a atribuição de um valor a uma célula.
    Requires:
      mundo é uma matriz de 0s e 1s formatada como descrito no contrato
        de cria_mundo, com pelo menos 2 linhas e 2 colunas;
      linha e coluna são os índices da linha e da coluna da célula que se quer
        afectar; o primeiro índice possível é 0 e o último é, respectivamente,
        (número de linhas) - 1 e (número de colunas) - 1
      valor é 0 ou 1.
    Side-effects: define o valor da célula na posição indicada.
    """
    pass # código a completar pelos alunos

def le_valor_celula(mundo, linha, coluna):
    """ Lê o valor de uma célula

    Requires:
      mundo é uma matriz de 0s e 1s formatada como descrito no contrato
        de cria_mundo, com pelo menos 2 linhas e 2 colunas;
      linha e coluna são os índices da linha e da coluna da célula que se quer
        ler; o primeiro índice possível é 0 e o último é, respectivamente,
        (número de linhas) - 1 e (número de colunas) - 1
    Ensures: 0 ou 1, conforme o valor da célula.
    """
    pass # código a completar pelos alunos

def itera_mundo(mundo, regra = (3, 2, 3)):
    """ Actualiza o estado de todas as células do mundo, de acordo com a regra

    As condições de fronteira são periódicas, ou seja:
      mundo[i][colunas] é o mesmo que mundo[i][0]
      mundo[i][-1] é o mesmo que mundo[i][colunas - 1] (já é assim no Python)
      mundo[linhas][j] é o mesmo que mundo[0][j]
      mundo[-1][j] é o mesmo que mundo[linhas - 1][j] (já é assim no Python)     
    Requires:
      mundo é uma matriz de 0s e 1s formatada como descrito no contrato
        de cria_mundo, com pelo menos 2 linhas e 2 colunas;
      regra é um triplo de int em que cada int está entre 0 e 8 inclusive.
    Side-effects: define o valor de cada célula do mundo para a iteração
      seguinte com a regra dada, alterando esse valor onde necessário.
    """
    pass # código a completar pelos alunos               

def itera_mundo_n_geracoes(n, mundo, regra = (3, 2, 3)):
    """ Itera o mundo n vezes, de acordo com a regra

    Requires:
      mundo é uma matriz de 0s e 1s formatada como descrito no contrato
        de cria_mundo, com pelo menos 2 linhas e 2 colunas;
      regra é um triplo de int em que cada int está entre 0 e 8 inclusive;
      n é um int positivo.
    Side-effects: define o valor com que cada célula do mundo fica após n
      iterações com a regra dada, alterando os valores onde necessário.
    """
    pass # código a completar pelos alunos

def mostra_mundo(mundo):
    """ Mostra o mundo no output standard (ecrã)

    Requires: mundo é uma matriz de 0s e 1s formatada como descrito no contrato
      de cria_mundo, com pelo menos 2 linhas e 2 colunas.
    Side-effects: imprime a matriz mundo no ecrã, linha a linha, representando
      cada 0 pela string ". " (ponto seguido de espaço) e
      cada 1 pela string "X " (x maiúsculo seguido de espaço);
      cada linha impressa termina com um espaço, que se segue a "." ou a "X".      
    """
    pass # código a completar pelos alunos

def escreve_mundo(mundo, nome_ficheiro):
    """ Regista o mundo num ficheiro

    Comporta-se como mostra_mundo, mas escrevendo num ficheiro em vez de no
      ecrã.
    Requires:
      mundo é uma matriz de 0s e 1s formatada como descrito no contrato
        de cria_mundo, com pelo menos 2 linhas e 2 colunas;
      nome_ficheiro é uma string que representa um path válido para um ficheiro.
    Side-effects:
      se o ficheiro nome_ficheiro existir, ele é reescrito; caso contrário,
        é criado um novo ficheiro de texto com esse path;
      a função imprime a matriz mundo no ficheiro, linha a linha, representando
        cada 0 pela string ". " (ponto seguido de espaço) e
        cada 1 pela string "X " (x maiúsculo seguido de espaço);
        cada linha impressa termina com um espaço, que se segue a "." ou a "X";
      não é feita programação defensiva, pelo que o programa terminará com erro
        se não for possível escrever num ficheiro com o path indicado.
    """
    pass # código a completar pelos alunos

def le_mundo(nome_ficheiro):
    """ Lê um mundo de um ficheiro

    Inicializa e devolve um novo mundo a partir de um ficheiro.
    Requires:
      nome_ficheiro é uma string que representa um path válido para um ficheiro
        de texto;
      o respectivo ficheiro está no mesmo formato indicado no contrato de
        escreve_ficheiro;
      os dados contidos no ficheiro permitem criar um matriz com pelo menos
        2 linhas e 2 colunas.
    Ensures: um mundo, ou seja, uma matriz de 0s e 1s formatada como descrito
      no contrato de cria_mundo, com pelo menos 2 linhas e 2 colunas.
    Side-effects: não é feita programação defensiva, pelo que o programa
      terminará com erro se não estiver acessível um ficheiro de texto com o
      path indicado e com formato de dados adequado.
    """
    pass # código a completar pelos alunos

def anima_mundo(n, mundo, regra = (3, 2, 3), atraso = 0.9): 
    """ Mostra uma animação do mundo no output standard (ecrã)

    Requires:
      mundo é uma matriz de 0s e 1s formatada como descrito no contrato
        de cria_mundo, com pelo menos 2 linhas e 2 colunas;
      regra é um triplo de int em que cada int está entre 0 e 8 inclusive;
      n é um int positivo;
      atraso é um float positivo.
    Side-effects:
      imprime a condição inicial dada para o mundo, e imprime depois n
      sucessivos fotogramas (frames) de uma animação da evolução do mundo a
      partir dessa condição inicial, usando a regra dada; em cada frame,
      imprime a matriz mundo no ecrã, linha a linha, representando
        cada 0 pela string ". " (ponto seguido de espaço) e
        cada 1 pela string "X " (x maiúsculo seguido de espaço);
        cada linha impressa termina com um espaço, que se segue a "." ou a "X".
      Antes de ser impresso o fotograma inicial (condição inicial), o ecrã é
      apagado.
      Cada fotograma sobrepõe-se ao anterior, que foi entretanto apagado.
      O tempo entre fotogramas é dado pelo valor de atraso em segundos.
      O último fotograma não é apagado de imediato. No final, surge no ecrã a
      questão "Terminar? (carregue em return)"; após o utilizador carregar em
      return, a função termina.
      Esta função altera o estado do mundo.
    """
    import os
    import time
    os.system('CLS')
    mostra_mundo(mundo)
    time.sleep(atraso)
    for _ in range(n):
        os.system('CLS')
        itera_mundo(mundo, regra)
        mostra_mundo(mundo)
        time.sleep(atraso)
    input("Terminar? (carregue em return)")
