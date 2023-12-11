import random
import vertex
import constraint

class generator:
    def __init__(self, N):
        self.N = N
        
    def generateAdjencyMatrixList(self, ConstraintsList):
        n = self.N
        AdjMatrList = []
        for k in ConstraintsList:
            verticies = []
            for i in range(n):
                routelist = [0]*n
                verticies.append(vertex.vertex(routelist))
            AdjMatrList.append(verticies)
        for k in range(len(ConstraintsList)):
            for i in range(n-1):
                for j in range(i+1, n):
                    AdjMatrList[k][i].pathList[j] = AdjMatrList[k][j].pathList[i] = random.randint(ConstraintsList[k].left,ConstraintsList[k].right)
        return AdjMatrList
    
    def printGraph(self):
        print(self.routeGraph)

    def generateUnavailableRode(self, roadLoad):
        indexes = random.sample(range(0, self.N), 2)
        roadLoad[indexes[0]].pathList[indexes[1]] = None
        roadLoad[indexes[1]].pathList[indexes[0]] = None
        

    def generateRandomPermutation(self, constraint):
        numbers = list(range(constraint.left, constraint.right + 1))
        random.shuffle(numbers)
        return numbers
    