class Nario:
    def __init__(self, valor, hijos=[]):
        self.valor = valor
        self.hijos = hijos

miNario = Nario(25, [Nario(10), Nario(100)])


def buscar(arbol, valor):
    if arbol.valor == valor:
        return True
    return buscarHijos(arbol.hijos, valor)

def buscarHijos(lista, valor):
    if lista==[]:
        return False
    return buscar(lista[0], valor) or buscarHijos(lista[1:], valor)

print(buscar(miNario, 25))


