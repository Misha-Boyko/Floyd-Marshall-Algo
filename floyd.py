#Floyd Marhsall Algorithm
import numpy as np
from Vertex import Vertex

#Initialize 2D array of size Vertex by Vertex for Distance:
#Initailize 2D array of size Vertex by Vertex for Previous:
#Base Case:
def intialize(vertices):
    distances = np.zeros((len(vertices),len(vertices)))
    previous = np.zeros((len(vertices),len(vertices)))
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if i == j:
                distances[i][j] = 0
            elif vertices[i].neighbors[j] == True:
                distances[i][j] = vertices[i].edgeWeights[j]
            else:
                distances[i][j] = float("inf")
            previous[i][j] = None
    return distances, previous

#initialize diagonals as distance 0
#initalize distance between vertices with an edge as the weight of the edge
#initialize all other distances as infinity

#Algorithm:
#Triple loop through k,i,j
#If distance[i][j] > distance[i][k] + distance[k][j]
#   distance[i][j] = distance[i][k] + distance[k][j]
#   previous[i][j] = previous[k][j]
#return distance, previous
def FloydAlgo(distances, previous, vertices, k):
    if k>=len(vertices):
        cap = len(vertices)
    else:
        cap = k
    for k in range(cap):
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    previous[i][j] = k
    DisplayTable(distances, previous)

def DisplayTable(distances, previous):
    print("Distances Table:")
    for i in range(len(vertices)):
        print(distances[i])
    print("Previous Table:")
    for i in range(len(vertices)):
        print(previous[i])

if __name__ == "__main__":
    print("Floyd Marshall Algorithm")
    a = Vertex("a", [True, True, True, True, True, False, False, False, False], [0, 5, 2, 4, 10, 0, 0, 0, 0])
    b = Vertex("b", [True, True, False, True, False, False, False, False, False], [5, 0, 0, 8, 0, 0, 0 ,0 ,0])
    c = Vertex("c", [True, False, True, False, True, True, False, False, False], [2, 0, 0, 0, 7, 5, 0, 0, 0])
    d = Vertex("d", [True, True, False, True, True, False, True, False, False], [4, 8, 0, 0, 6, 0, 2, 0, 0])
    e = Vertex("e", [True, False, True, True, True, True, True, True, False], [10, 0, 7, 6, 0, 3, 2, 3, 0])
    f = Vertex("f", [False, False, True, False, True, True, False, True, True], [0, 0, 5, 0, 3, 0, 0, 2, 4])
    g = Vertex("g", [False, False, False, True, True, False, True, True, False], [0, 0, 0, 2, 2, 0, 0, 3, 0])
    h = Vertex("h", [False, False, False, False, True, True, True, True, True], [0, 0, 0, 0, 3, 2, 3, 0, 5])
    i = Vertex("i", [False, False, False, False, False, True, False, True, True], [0, 0, 0, 0, 0, 4, 0, 5, 0])

    vertices = [a, b, c, d, e, f, g, h, i]
    intialized = intialize(vertices)
    distances = intialized[0]
    previous = intialized[1]

    FloydAlgo(distances, previous, vertices, 1)
    FloydAlgo(distances, previous, vertices, 2)
    FloydAlgo(distances, previous, vertices, 6)
    FloydAlgo(distances, previous, vertices, 9)
    #some funciton to display table results of distances and previous:


