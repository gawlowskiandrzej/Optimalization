import itertools
import random

class tspProblem:
    def __init__(self, N):
        self.N = N

    def CheckIfMin(self,dist, min):
        #sprawdzanie czy wystąpiło minimum
        if dist < min:
            return True
        else:
            return False
    
    def CheckIfAvailebale(self,elem):
        #sprawdzanie czy dana ścieżka jest dostępna
        if (elem is None):
            return False
        else:
            return True
        
    def calculateTimeToTravel(self,AdjMatrix, i, j):
        #zliczanie czasu potrzebnego do pokonania ścieżki wyznacznik
        distance = AdjMatrix[0][i].pathList[j]
        roadLoad = AdjMatrix[1][i].pathList[j]
        if not self.CheckIfAvailebale(roadLoad):
            return -1
        else:
            return round(distance*(round(roadLoad/10,2)),2)

    def TSPBruteForce(self, AdjMatrix):
        bestRoute = [0]*self.N
        min = float("inf")
        #przeszukiwanie całej puli rozwiązań
        for i in itertools.permutations(list(range(self.N))):

            overallTime = 0
            vertexList = []
            permutation = list(i)
            isAvaileble = True
            for j in range(self.N-1):
               time = self.calculateTimeToTravel(AdjMatrix, permutation[j], permutation[j+1])
               vertexList.append((permutation[j],permutation[j+1]))
               if time>-1:
                    overallTime += time
               else:
                    isAvaileble = False
                    break
            #sprawdzenie czy nie wystąpiła ścieżka z niedostępnym wieszchołkiem jeżeli tak pomiń
            if isAvaileble == False:
                continue
            #sprawdzenie czy droga do początkowego wieszchołka jest możliwa
            time = self.calculateTimeToTravel(AdjMatrix, permutation[-1], permutation[0])
            if time > -1:
                vertexList.append((permutation[-1],permutation[0]))
                overallTime += time
            else:
                continue

            if self.CheckIfMin(overallTime, min) == True:
                bestRoute = permutation
                min = overallTime
        return bestRoute, min
    
    def TSPGreedy(self, adjmatrix):
        visited = [False]*self.N
        best_path = []
        otime = 0
        start = 0
        best_path.append(0)
        curr = start
        visited[0] = True

        for i in range(self.N-1):
            min_time = float('inf')
            next_vertex = None

            for neightbor in range(self.N):
                time = self.calculateTimeToTravel(adjmatrix,curr,neightbor)
                if time > -1 and not visited[neightbor] and time < min_time:
                    min_time = time
                    next_vertex = neightbor
            #jeżeli nie znalazł drogi do przejscia dalej, kończ algorytm z brakiem rozwiązania
            if next_vertex is None:
                return []
            curr = next_vertex
            best_path.append(curr)
            otime += min_time
            visited[curr] = True
        #sprawdź czy ścieżka do początkowego wieszchołka jest przejezdna, jeżeli nie to kończ algorytm
        time = self.calculateTimeToTravel(adjmatrix, curr, start)
        if time > -1:
            best_path.append(start) 
            otime += time
        else:
            return []
        return best_path, otime

    def TSPGreedyRandomise(self,adjmatrix, iterators):
        #ulosowiony zachłanny
        visited = [False]*self.N
        best_path = []

        start = 0
        best_path.append(0)
        curr = start
        otime = 0
        visited[0] = True

        for i in iterators[0:len(iterators)-1]:
            min_time = float('inf')
            next_vertex = None
            #generuj losową kolejność wieszchołków
            random.shuffle(iterators)
            for neighbour in iterators:
                time = self.calculateTimeToTravel(adjmatrix,curr,neighbour)
                if time > -1 and not visited[neighbour] and time < min_time:
                    min_time = time
                    next_vertex = neighbour

            if next_vertex is None:
                return []
            curr = next_vertex
            best_path.append(curr)
            visited[curr] = True
            otime+=min_time

        time = self.calculateTimeToTravel(adjmatrix, curr, start)
        if time > -1:
            best_path.append(start) 
            otime += time
        else:
            return []
        return best_path, otime