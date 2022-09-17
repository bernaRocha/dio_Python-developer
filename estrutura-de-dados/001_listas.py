from os import system
system('clear')

frutas = []
frutas = ['Laranja', 'Maça', 'Uva', 'Banana']

letras = list('python')
print(letras[0]) # p
print(letras[-1]) # n

tamanho = list(range(10))
print(tamanho) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

matriz = [
    [1, 'a', 2],
    ['r', 5, 2],
    [0, 'z', 2]
]

print(matriz[0]) # [1, 'a', 2]
print(matriz[0][0]) # 1
print(matriz[0][-1]) # 2
print(matriz[-1][-1]) # 2

# fatiamento

frase = "frase para treinar fatiamento"
print(frase[2:]) # ase para treinar fatiamento
print(frase[2:7]) # ase p
print(frase[:6]) # frase

lista = ["p", "y", "t", "h", "o", "n"]
print(lista[::-1]) # ['n', 'o', 'h', 't', 'y', 'p']
print(lista[::-2]) # ['n', 'h', 'y']

kaiju = ["Mothra", "Godzilla", "King guidorah", "Rodan"]

for indice, monstro in enumerate(kaiju):
    print(f'{indice + 1}: {monstro}')

'''
1: Mothra
2: Godzilla
3: King guidorah
4: Rodan
'''

numeros = [1, 67, 43, 22, 68, 92, 0, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares) # [22, 68, 92, 0, 34]

pares = [numero for numero in numeros if numero % 2 == 0]

# modificando
numeros = [1, 67, 43, 22, 68, 92, 0, 34]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado) # [1, 4489, 1849, 484, 4624, 8464, 0, 1156]

outra_lista = []

outra_lista.append(1)
outra_lista.append('Rust')
outra_lista.append(['Javascript', 'C#'])
print(outra_lista) # [1, 'Rust', ['Javascript', 'C#']]
outra_lista.clear()
print(outra_lista) # []

lista2 = lista.copy()
print(lista2) # ['p', 'y', 't', 'h', 'o', 'n']
lista2[4] = '@'
print(lista2) # ['p', 'y', 't', 'h', '@', 'n']

linguagens = ['python', 'csharp', 'java', 'golang', 'C']
print(linguagens) # ['python', 'csharp', 'java', 'golang', 'C']
linguagens.extend(['HTML', 'CSS', 'C'])
print(linguagens) # ['python', 'csharp', 'java', 'golang', 'C', 'HTML', 'CSS', 'C']

print(linguagens.index('C')) # 4 -> Só o primeiro caso tenha repetição
print(linguagens.index('HTML')) # 5

linguagens.remove('CSS')
print(linguagens) # ['python', 'csharp', 'java', 'golang', 'C', 'HTML', 'C']
linguagens.reverse()
print(linguagens) # ['C', 'HTML', 'C', 'golang', 'java', 'csharp', 'python']

linguagens.sort(key=lambda x: len(x))
print(linguagens) # ['C', 'C', 'HTML', 'java', 'golang', 'csharp', 'python']

linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens) # ['golang', 'csharp', 'python', 'HTML', 'java', 'C', 'C']
