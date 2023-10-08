from queue import Queue
from agente import Agente
import manager as mn
from graphviz import Digraph

mapa = [
    ['', 'uta', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', 'mall', ''],
]


puntoInicial = mn.obtenerUbicacion('uta', mapa)
puntoObjetivo = mn.obtenerUbicacion('mall', mapa)
print(f'UTA {puntoInicial}')
print(f'MALL {puntoObjetivo}')

raiz = Agente()
raiz.inicio(mapa, puntoInicial, puntoObjetivo)
raiz.controlarRepetidos = True #activo el control de los repetidos

grafo = Digraph()
pila = []
pila.append(raiz)

solucion:Agente = None
print('buscando solucion ...')
while len(pila) > 0:
    estadoActual:Agente = pila.pop() # pop retorna el ultimo elemento agregado y lo elimina de la pila
    grafo.node(estadoActual.obtenerID(), estadoActual.obtenerID()) #parte grafica
    if estadoActual.esObjetivo(): # control si es objetivo
        solucion = estadoActual
        grafo.node(estadoActual.obtenerID(), estadoActual.obtenerID())
        print('solucion encontrada ...')
        break
    nuevosEstados = mn.ejecutarMovimientos(mn.generarHijos(estadoActual, 4))
    for nuevo in nuevosEstados:
        grafo.node(nuevo.obtenerID(), nuevo.obtenerID())
        grafo.edge(estadoActual.obtenerID(), nuevo.obtenerID())
        pila.append(nuevo)
        
mapaVacio = mn.dibujarMapaVacio(len(mapa), len(mapa[0]))
mn.dibujarRutaSolucion(solucion, mapaVacio)
solucion.mostrarcaminoRecorrido()
grafo.render("arbol_busqueda", view=True)
