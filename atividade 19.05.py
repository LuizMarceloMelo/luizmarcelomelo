
#subprograma para remover os caracteres especiais

def remover_especiais(old, to_remove):
    palavra = old
    for x in to_remove:
        palavra = palavra.replace(x, "")
    return palavra


#subprograma para verificar o total de palavras

def total_palavras():             

    print ("O total de palavras é:", len(lista),"\n")

    
#subprograma para encontrar as 5 maiores palavras

def maiores_palavras(n):

    dict={}

    for q in lista:
        lista.count(q)
        dict[q]=lista.count(q)
    
    lista2 =[]

    for x, y in dict.items():
    
        z= (len(x),x)
        lista2.append (z)

    ordenada = sorted(lista2)

    reversa = list (reversed(ordenada))

    maiores = 0

  
    print ("As maiores palavras são: ","\n")

    while maiores <n:
        
        h1 = reversa[maiores]
        print (h1[1],'=', h1[0], 'letras')
        maiores += 1
    print ("\n")


#subprograma para encontrar a vogal que mais aparece

def vogal (lista_vogal):
    vogais = []
    for i in range (len(lista_vogal)):

        a = lista_vogal[i]
        b = texto.count(a)       
        c = (b,a)

        vogais.append (c)
    ordenada2 = sorted (vogais)

    h3 = ordenada2[4]

    print ("A vogal que mais aparece é: ",h3[1], "\n")


#subprograma para verificar a literal "ção"

def literal(x):
    for i in range (len(lista)):
        if x in Linha[i]:
            print("O trecho - ", x, " - aparece primeiro na linha", i+1)
            break    


#abrir e ler o arquivo de texto

arquivo = open ('texto.txt', 'r', encoding='utf-8')
texto = arquivo.read()


#separar o texto por linhas

Linha = texto.split("\n")


lista = []

for i in range (len(Linha)):

# remover os caracteres especiais

    for g in (texto):
        texto2=remover_especiais(Linha[i], ',"*:.$(#')

# fazer uma lista com as palavras
      
    for palavras in texto2.split(" "):
            lista.append(palavras)


#Objetivo 1
total_palavras()

#Objetivo 2
maiores_palavras(5)

#Objetivo 3
lista_vogal = ['a','e','i','o','u']
vogal (lista_vogal)  

#Objetivo 4
literal("ção")
