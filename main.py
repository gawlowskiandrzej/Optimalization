import generator
import tspProblem
import constraint
import copy
import drawer
import vertex
import time
import matplotlib.pyplot as plt
import json

#en = generator.generator(5)
#adjMatrixwothoutRoad = gen.generateAdjencyMatrixList([constraint.constraint(1,4), constraint.constraint(1,1)])
#adjMatrixwithallRoads = copy.deepcopy(adjMatrixwothoutRoad)
#gen.generateUnavailableRode(adjMatrixwothoutRoad[1])
'''
print("Macierz z wszystkimi: ")
for i in adjMatrixwithallRoads[1]:
    print(i.pathList)
print("   ")
print("Macierz bez wszystkich: ")
for i in adjMatrixwothoutRoad[1]:
    print(i.pathList)
print("   ")
'''
def serialize_vertex(Vertex):
    if isinstance(Vertex, vertex.vertex):
        return {'pathList': Vertex.pathList}
    raise TypeError(f"Object of type {type(vertex)} is not JSON serializable")
def deserialize_vertex(obj):
    if 'pathList' in obj:
        return vertex.vertex(obj['pathList'])
    return obj
#problem = tspProblem.tspProblem(gen.N)
timetable1 = []
timetable2 = []
timetable3 = []
adjMatrixwithallRoads = []
with open('dane.json', 'r') as file:
    adjMatrixwithallRoads = json.load(file, object_hook=deserialize_vertex)

'''
for i in range(3,9):
    gen = generator.generator(i)
    adjMatrixwothoutRoad = gen.generateAdjencyMatrixList([constraint.constraint(1,4), constraint.constraint(1,1)])
    adjMatrixwithallRoads = copy.deepcopy(adjMatrixwothoutRoad)
    gen.generateUnavailableRode(adjMatrixwothoutRoad[1])
    problem = tspProblem.tspProblem(i)
    timetable1.append(problem.TSPBruteForce(adjMatrixwithallRoads)[1])
    timetable2.append(problem.TSPGreedywithUnAvailabeRode(adjMatrixwithallRoads)[1])
    timetable3.append(problem.TSPGreedyRandomise(adjMatrixwithallRoads, list(range(i)))[1])
'''
#with open('dane.json', 'w') as file:
    #json.dump(adjMatrixwothoutRoad, file,default=serialize_vertex, indent=3)
'''
tab = problem.TSPBruteForce(adjMatrixwothoutRoad)
if len(tab) < (gen.N):
    print("Brak rozwiązania dla algorytmu bruteForce")
else:
    print(tab)
'''
#timeT = time.time()
#problem.TSPGreedywithUnAvailabeRode(adjMatrixwithallRoads)
#timetable.append(timeT-time.time())
'''
tab = problem.TSPGreedywithUnAvailabeRode(adjMatrixwothoutRoad)
if len(tab) < (gen.N + 1):
    print("Brak rozwiązania dla algorytmu")
else:
    print(tab)
'''
#timeT = time.time()
#problem.TSPGreedyRandomise(adjMatrixwithallRoads,list(range(gen.N)))
#timetable.append(timeT-time.time())
'''
tab = problem.TSPGreedyRandomise(adjMatrixwothoutRoad,list(range(gen.N)))
if len(tab) < (gen.N + 1):
    print("Brak rozwiązania dla algorytmu")
else:
    print(tab)
'''

#dr = drawer.drawer()
#dr.drawGraph(adjMatrixwithallRoads[0], adjMatrixwithallRoads[1])
plt.plot(list(range(3,9)), timetable1, label='BruteForce')
plt.plot(list(range(3,9)), timetable2, label='Greedy')
plt.plot(list(range(3,9)), timetable3, label='RandomGreedy')
#plt.plot(list(range(1,gen.N)), timetable[1], label='Greedy')
#plt.plot(list(range(1,gen.N)), timetable[2], label='GreedyRandomise')

plt.xlabel('Numer of vertexes')
plt.ylabel('Distances')

plt.title("Wykres funkcji TSP")

plt.legend()

plt.show()
#problem.TSPBruteForce(adjMatrixList)
#problem.TSPBruteForce(adjMatrixList[0])
#problem.TSPGreedy(adjMatrixList[0])
#problem.TSPGreedyRandomise(adjMatrixList[0],gen.generateRandomPermutation(constraint.constraint(0,gen.N-1)))