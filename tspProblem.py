import itertools
import random

class tspProblem:
    def __init__(self, N):
        self.N = N

    def CheckIfMin(self,dist, min):
        if dist < min:
            return True
        else:
            return False
    
    def CheckIfAvailebale(self,elem):
        if (elem is None):
            return False
        else:
            return True
        
    def calculateTimeToTravel(self,AdjMatrix, i, j):
        distance = AdjMatrix[0][i].pathList[j]
        roadLoad = AdjMatrix[1][i].pathList[j]
        if not self.CheckIfAvailebale(roadLoad):
            return -1
        else:
            return round(distance*(round(roadLoad/10,2)),2)

    def TSPBruteForce(self, AdjMatrix):
        bestRoute = [0]*self.N
        min = float("inf")
        
        for i in list(itertools.permutations(list(range(self.N)))):

            overallTime = 0
            vertexList = []

            for j in range(self.N-1):
               time = self.calculateTimeToTravel(AdjMatrix, i[j], i[j+1])
               vertexList.append((i[j],i[j+1]))
               if time>0:
                    overallTime += time
               else:
                    break
               
            time = self.calculateTimeToTravel(AdjMatrix, i[-1], i[0])
            if time > 0:
                vertexList.append((i[-1],i[0]))
                overallTime += time
            else:
                continue

            if self.CheckIfMin(overallTime, min) == True:
                bestRoute = i
                min = overallTime
        return bestRoute, min
    '''
    def TSPBruteForcewithUnAvailabe(self, adjmatrix):
        bestRoute = [0]*self.N
        min = float("inf")
        
        for i in list(itertools.permutations(list(range(self.N)))):

            overallDist = 0
            distList = []
            isAvaileble = True

            for j in range(self.N-1):
               if distances[i[j]].pathList[i[j+1]] is None:
                   isAvaileble = False
                   break
               distList.append(distances[i[j]].pathList[i[j+1]])
               overallDist += distances[i[j]].pathList[i[j+1]]

            if isAvaileble == False:
                continue
            if distances[i[-1]].pathList[i[0]] != None:
                distList.append(distances[i[-1]].pathList[i[0]])
                overallDist += distances[i[j]].pathList[i[j+1]]
            else:
                continue

            if self.CheckIfMin(overallDist, min) == True:
                bestRoute = i
                min = overallDist
        return bestRoute'''
    
    def TSPGreedy(self, distances):
        visited = [False]*self.N
        best_path = []

        start = 0
        best_path.append(0)
        curr = start
        visited[0] = True

        for i in range(self.N-1):
            min_dist = float('inf')
            next_city = None

            for neightbor in range(self.N):
                if  not visited[neightbor] and distances[curr].pathList[neightbor] < min_dist:
                    min_dist = distances[curr].pathList[neightbor]
                    next_city = neightbor
            
            curr = next_city
            best_path.append(curr)
            visited[curr] = True
        
        best_path.append(start) 
    
    def TSPGreedywithUnAvailabeRode(self, adjmatrix):
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
            if next_vertex is None:
                return []
            curr = next_vertex
            best_path.append(curr)
            otime += min_time
            visited[curr] = True
        
        time = self.calculateTimeToTravel(adjmatrix, curr, start)
        if time > -1:
            best_path.append(start) 
            otime += time
        else:
            return []
        return best_path, otime

    def TSPGreedyRandomise(self,adjmatrix, iterators):
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
            random.shuffle(iterators)
            for neightbor in iterators:
                time = self.calculateTimeToTravel(adjmatrix,curr,neightbor)
                if time > -1 and not visited[neightbor] and time < min_time:
                    min_time = time
                    next_vertex = neightbor

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