def index_of_by_index(word, list, index):
    for indice in range(index, len(list)):
        if list[indice]==word:
            return indice
    return -1
colors=["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(index_of_by_index("Black", colors, 1))
print(index_of_by_index("Black", colors, 4))
print(index_of_by_index("Green", colors, 2))


def index_of_empty(list):
    for indice, valor in enumerate(list):
        if valor == "":
            return indice
    return -1
colors = ["Red","Green","White","Black","Pink","Yellow","Black"]
print(index_of_empty(colors))


def index_of(word, list):
    for indice, valor in enumerate(list):
        if valor == word:
            return indice
    return -1
colors = ["Red","Green","White","Black","Pink","Yellow","Black"]
print(index_of("Black", colors))
print(index_of("Blue", colors))


def put(word, list):
    for indice, valor in enumerate(list):
        if valor == '':
            list[indice]=word
            return indice
    return -1
colors = ["Red","Green","","","Pink","","Black"]
print(put("Black", colors))


def remove(word,list):
    cuenta = 0 
    for indice in range(len(list)):
        if list[indice] == word:
            list[indice] = ""
            cuenta = cuenta + 1
    return cuenta
colors = ["Red","Green","White","Black","Pink","Yellow","Black"]
print(remove("Black",colors))
print(remove("Blue",colors))
