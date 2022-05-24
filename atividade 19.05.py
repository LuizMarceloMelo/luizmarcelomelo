def remover_especiais(old, to_remove):
    palavra = old
    for x in to_remove:
        palavra = palavra.replace(x, "")
    return palavra


def total_palavras():             

    print ("O total de palavras é:", len(lista2),"\n")


def maiores_palavras(n):
    dict={}

    for q in lista2:
        lista2.count(q)
        dict[q]=lista2.count(q)
    
    lista3 =[]

    for x, y in dict.items():
    
        z= (len(x),x)
        lista3.append (z)

    ordenada = sorted(lista3)

    reversa = list (reversed(ordenada))

    maiores = 0

    h1 = []

    print ("As maiores palavras são: ","\n")

    while maiores <n:

        h1.append (reversa[maiores])
   
        maiores += 1

    return print(h1, "\n")   

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



def literal(x):
    for i in range (len(lista2)):
        if x in Linha[i]:
            print("O trecho - ", x, " - aparece primeiro na linha", i+1)
            break    




arquivo = open ('texto.txt', 'r', encoding='utf-8')
texto = arquivo.read()

Linha = texto.split("\n")


contador_de_linhas = 0
    
for i in Linha:
    if i:
        contador_de_linhas += 1

lista2 = []

for i in range (contador_de_linhas):
    
    for g in (texto):
        texto2=remover_especiais(Linha[i], ',"*:.$(#')
        
    for palavras in texto2.split(" "):
            lista2.append(palavras)


#Objetivo 1
total_palavras()

#Objetivo 2
maiores_palavras(5)

#Objetivo 3
lista_vogal = ['a','e','i','o','u']
vogal (lista_vogal)  

#Objetivo 4
literal("ação")
