# Importação das classes de palavras para serem aplicadas no jogo
from palavras import frutas_verduras_legumes
from palavras import países
from palavras import cores
import random

# Estágios de cada fase da forca
def exibir_forca(tentativas):
  estagios = [  # Fim de jogo
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
                  -
              """,
              # Falta 1 tentativa
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / 
                  -
              """,
              # Faltam 2 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |      
                  -
              """,
              # Faltam 3 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |     
                  -
              """,
              # Faltam 4 tentativas
              """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
              """,
              # Faltam 5 tentativas
              """
                  --------
                  |      |
                  |      O
                  |    
                  |      
                  |     
                  -
              """,
              # Estado inicial
              """
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
              """
  ]

  return estagios[tentativas]

# Inicialização do jogo
print('OLÁ! BEM VINDO AO JOGO DA FORCA!')
def escolha():
   classe = int(input('ESCOLH A CLASSE DE PALAVRAS QUE SERÃO ESCOLHIDAS PARA ESTE JOGO: '
                    ' \n 1 - Frutas, verduras e legumes. '
                    ' \n 2 - Países. '
                    ' \n 3 - Cores '))
   match classe:
    case 1:
      classe = frutas_verduras_legumes
    case 2:
      classe = países
    case 3:
      classe = cores
   return classe

classe = escolha()

# Selecionar a palavra
def selecionar_palavras():
    palavra = random.choice(classe)
    return palavra.upper()
palavra = selecionar_palavras()

# Iniciar o jogo
# len_palavra = Palavra censurada (sendo formada).
# letras_uti = Conjunto de letras que já foram utilizadas.
# palavras_uti = Conjunto de palavras que já foram utilizadas.
# letras_adi = Conjunto de letras acentudas, que podem estar contidas na palavra.
def jogar(palavra):
   len_palavra = '_' * len(palavra)
   letras_uti = []
   palavras_uti = []
   adivinhou = False
   tentativas = 6
   letras_adi = ['Á','Â','Ã','É','Ê','Í','Ó','Ô','Õ','Ú','Ç']

   # Introdução do jogo
   print('VAMOS JOGAR!')
   print(exibir_forca(tentativas))
   print('Esta palavra é: ',len_palavra)

   # Looping para tentativas de um única letra
   while adivinhou is False and tentativas > 0:
      tentativa = input('Digite uma letra ou uma tentativa de palavra completa: ').upper()
      if len(tentativa) == 1 and tentativa.isalpha(): 
       
       # Possibilidade para substituição automática de letras caso a palavra contenha "-"
       if '-' in palavra:
         palavra_lista = list(len_palavra)
         indices = [i for i, letra in enumerate(palavra) if letra == '-']
         for indice in indices:
            palavra_lista[indice] = '-'
            len_palavra = ''.join(palavra_lista)
       
       # Possibilidade para substituição automática de letras caso a palavra contenha " " (Espaço)
       if ' ' in palavra:
         palavra_lista = list(len_palavra)
         indices = [i for i, letra in enumerate(palavra) if letra == ' ']
         for indice in indices:
            palavra_lista[indice] = ' '
            len_palavra = ''.join(palavra_lista)

       # Tentativa para letras repetidas 
       if tentativa in letras_uti:
         print('Você ja utilizou essa letra antes')
       
       # Tentativas incorretas
       elif tentativa not in palavra:
        if 'Á' or 'Â' or 'Ã' or 'É' or 'Ê' or 'Í' or 'Ó' or 'Ô' or 'Õ' or 'Ú' or 'Ç' not in palavra: 
         print('Letra não faz parte da palavra, você perdeu uma tentativa.')
         tentativas -= 1
         letras_uti += [tentativa]
           
         # Tentativas insuficientes
         if tentativas == 0:
          print('Acabaram as tentativas')
          print('A palavra correta era: [',palavra,']')
        
       # Tentativas corretas
       # Looping for para substituir "_" por letras corretas
       elif tentativa in palavra:
          letras_uti += [tentativa]
          palavra_lista = list(len_palavra)
          indices = [i for i, letra in enumerate(palavra) if letra == tentativa]
          for indice in indices:
            palavra_lista[indice] = tentativa
            len_palavra = ''.join(palavra_lista)
            print('Voce acertou uma letra! [',tentativa,']')

       # IF para selecionar os caracteres ['A','E','I','O','U','C'], para caso a palavra tenha uma letra acentuada.
       if tentativa in ['A','E','I','O','U','C']:
           
        # Loop for para verificar se a uma letra acentuada na palavra e em qual posição ela se situa.
        for x in letras_adi:
         if x in palavra:
          tentativa2 = x  

          # Loop para transformar o caracter 'A' em uma letra acentuada e assim por diante ['A','E','I','O','U','C'].       
          if tentativa == 'A' and tentativa2 in ['Á','Ã','Â']:
           letras_uti += [tentativa]
           letras_uti += [tentativa2]
           palavra_lista2 = list(len_palavra)
           indices2 = [i for i, letra in enumerate(palavra) if letra == tentativa2]
           for indice in indices2:
            palavra_lista2[indice] = tentativa2
            len_palavra = ''.join(palavra_lista2)
            print('Você acertou uma letra! [',tentativa,']')      
                   
          if tentativa == 'E' and tentativa2 in ['É','Ê']:
           letras_uti += [tentativa]
           letras_uti += [tentativa2]
           palavra_lista2 = list(len_palavra)
           indices2 = [i for i, letra in enumerate(palavra) if letra == tentativa2]
           for indice in indices2:
            palavra_lista2[indice] = tentativa2
            len_palavra = ''.join(palavra_lista2)        
            print('Você acertou uma letra! [',tentativa,']')

          if tentativa == 'I' and tentativa2 in ['Í']:
           letras_uti += [tentativa]
           letras_uti += [tentativa2]
           palavra_lista2 = list(len_palavra)
           indices2 = [i for i, letra in enumerate(palavra) if letra == tentativa2]
           for indice in indices2:
            palavra_lista2[indice] = tentativa2
            len_palavra = ''.join(palavra_lista2)
            print('Você acertou uma letra! [',tentativa,']')
                    
          if tentativa == 'O' and tentativa2 in ['Ó','Õ','Ô']: 
           letras_uti += [tentativa]
           letras_uti += [tentativa2]
           palavra_lista2 = list(len_palavra)
           indices2 = [i for i, letra in enumerate(palavra) if letra == tentativa2]
           for indice in indices2:
            palavra_lista2[indice] = tentativa2
            len_palavra = ''.join(palavra_lista2)
            print('Você acertou uma letra! [',tentativa,']')    

          if tentativa == 'U' and tentativa2 in ['Ú']:
           letras_uti += [tentativa]
           letras_uti += [tentativa2]
           palavra_lista2 = list(len_palavra)
           indices2 = [i for i, letra in enumerate(palavra) if letra == tentativa2]
           for indice in indices2:
            palavra_lista2[indice] = tentativa2
            len_palavra = ''.join(palavra_lista2)
            print('Você acertou uma letra! [',tentativa,']')
               
          if tentativa == 'C' and tentativa2 in ['Ç']:
           letras_uti += [tentativa]
           letras_uti += [tentativa2]
           palavra_lista2 = list(len_palavra)
           indices2 = [i for i, letra in enumerate(palavra) if letra == tentativa2]
           for indice in indices2:
            palavra_lista2[indice] = tentativa2
            len_palavra = ''.join(palavra_lista2)
            print('Você acertou uma letra! [',tentativa,']') 
          
      
      # Opção incorreta para tentativas númericas ou algarismos          
      else: 
        if not tentativa.isalpha():
         print('Opção incorreta, digite apenas letras ou palavras.')

      # Número de letras corretas completadas
      if len_palavra == palavra:
        adivinhou = True
        print('FIM DE JOGO, VOCÊ COMPLETOU!')

      # Tentativas de acertar a palavra inteira e apenas com letras
      if len(tentativa) == len(palavra) and tentativa.isalpha():
        if tentativa == palavra:
          adivinhou = True
          print('VOÇÊ ACERTOU A PALAVRA!')
          print('A palavra correta era: [',palavra,']')
          print('FIM DE JOGO, VOCÊ COMPLETOU!')

        # Tentativa para palavras erradas repetidas
        if tentativa in palavras_uti:
          print('Você já utilizou esta palavra.')

        # Tentativa de acerto de palavra incorreta
        elif tentativa != palavra:
          print('Essa palavra não é a correta, você perdeu uma tentativa.')
          palavras_uti += [tentativa]
          tentativas -= 1  
        
        # Tentativas insuficientes
        if tentativas == 0:
          print('Acabaram as tentativas')
          print('A palavra correta era: [',palavra,']')
      
      # Descrição atualizada das informações do jogo
      print(exibir_forca(tentativas))
      print('Esta palavra é: ',len_palavra)
               
jogar(palavra)

# Opção para jogar novamente
novo = int(input('Deseja jogar novamente? '
                ' \n 1 - SIM '
                 '\n 2 - NÃO'))

# Looping While para jogar novamente até a resposta for 2 - (NÃO)
while novo == 1:
   classe = escolha()
   palavra = selecionar_palavras()
   jogar(palavra)
   novo = int(input('Deseja jogar novamente? '
                ' \n 1 - SIM '
                 '\n 2 - NÃO'))
print('FIM DE JOGO.'
'\nOBRIGADO POR JOGAR!')
