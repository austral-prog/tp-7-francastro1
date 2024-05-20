def enumerate_list(lista):
    lista_enumerada = []
    for indice, valor in enumerate(lista):
        if valor: 
            lista_enumerada.append(f"{len(lista_enumerada)}. {valor.title()}")
    return lista_enumerada
colors = ["Red","Green","","White","Black",""]
lista_enumerada = enumerate_list(colors)
print(lista_enumerada)

def enumerate_backwards(lista):
    lista_invertida = []
    for indice, valor in enumerate(lista):
        if valor: 
            lista_invertida.append(f"{len(lista_invertida)}. {valor[::-1]}")
    return lista_invertida
colors = ["Red","Green","","White","Black",""]
lista_invertida = enumerate_backwards(colors)
print(lista_invertida)
