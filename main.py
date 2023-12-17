import generator
import tspProblem
import constraint
import copy
import drawer
import vertex
import time
import matplotlib.pyplot as plt
import json

#funkcja umożliwiająca zapisanie obiektu jako tekst json
def serialize_vertex(Vertex):
    if isinstance(Vertex, vertex.vertex):
        return {'pathList': Vertex.pathList}
    raise TypeError(f"Object of type {type(vertex)} is not JSON serializable")

#funkcja umożliwiająca odczyt tekstu json jako obietku python
def deserialize_vertex(obj):
    if 'pathList' in obj:
        return vertex.vertex(obj['pathList'])
    return obj

#główna funkcja
def solveModifyTSPForN(N):
    adjMatrixwithallRoads = []
    adjMatrixwothoutRoad = []
    '''
    timetable1 = []
    timetable2 = []
    timetable3 = []
    '''
    #pętle do zczytywania danych
    with open(f'dane with road-{N}.json', 'r') as file:
        adjMatrixwithallRoads = json.load(file, object_hook=deserialize_vertex)
    with open(f'dane without road-{N}.json', 'r') as file:
        adjMatrixwothoutRoad = json.load(file, object_hook=deserialize_vertex)
    for i in range(N,N+1):

        #generator danych wejsciowych dla N wieszchołków
        #gen = generator.generator(i)

        #generowanie macierzy przy ograniczeniach 1 / macierz dystansów 2 / macierz obciążeń ścieżek
        #adjMatrixwothoutRoad = gen.generateAdjencyMatrixList([constraint.constraint(1,4), constraint.constraint(1,3)])
        #adjMatrixwithallRoads = copy.deepcopy(adjMatrixwothoutRoad)

        #generowanie nie przejezdnej ścieżki
        #gen.generateUnavailableRode(adjMatrixwothoutRoad[1])

        problem = tspProblem.tspProblem(i)
        print(problem.TSPBruteForce(adjMatrixwithallRoads))
        print(problem.TSPBruteForce(adjMatrixwothoutRoad))
        print(problem.TSPGreedy(adjMatrixwithallRoads))
        print(problem.TSPGreedy(adjMatrixwothoutRoad))
        print(problem.TSPGreedyRandomise(adjMatrixwithallRoads, list(range(i))))
        print(problem.TSPGreedyRandomise(adjMatrixwothoutRoad, list(range(i))))
    
    #obiekt rysujący grafy dla wszystkich przejezdnych i nie przejezdynch
    dr = drawer.drawer()
    dr.drawGraph(adjMatrixwothoutRoad[0], adjMatrixwothoutRoad[1])
    dr.drawGraph(adjMatrixwithallRoads[0], adjMatrixwithallRoads[1])
    '''
    plt.plot(list(range(5,11)), timetable1, label='BruteForce')
    plt.plot(list(range(5,11)), timetable2, label='Greedy')
    plt.plot(list(range(5,11)), timetable3, label='RandomGreedy')

    plt.xlabel('Numer of vertexes')
    plt.ylabel('Time returned from algorithms')

    plt.title("Wykres funkcji TSP")

    plt.legend()

    plt.show()
    '''

solveModifyTSPForN(9)

#zapis danych do pliku
#with open('dane without road-9.json', 'w') as file:
    #json.dump(adjMatrixwothoutRoad, file,default=serialize_vertex, indent=3)
#with open('dane with road-9.json', 'w') as file:
    #json.dump(adjMatrixwithallRoads, file,default=serialize_vertex, indent=3)
