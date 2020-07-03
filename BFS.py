
import numpy as np
import queue

map = np.loadtxt("map.txt", dtype=str, delimiter=' ')

start = 'Arad'
end = 'Bucharest'


def solution(neighbors, start, end):
    for x in neighbors:
        if(start == x[0] and end == x[len(x)-1]):
            return x


def BFS(start, end):
    fringe = queue.Queue()
    closed = queue.Queue()
    fringe.put(start)

    paths = []
    while(fringe.empty() == False):
        current = fringe.get()
        if current not in list(closed.queue):
            closed.put(current)
        if current == end:
            # print("_________________", paths)
            return solution(paths, start, end)
        else:
            temp = ''
            for x in map:
                if x[0] == current:
                    neighbors = [current]
                    if x[1] not in list(closed.queue):
                        fringe.put(x[1])
                        temp = x[1]
                        neighbors.append(x[1])
                        paths.append(neighbors)
            for y in paths:
                if y[len(y)-1] == current:
                    y.append(temp)

        print("-----fringe-------", list(fringe.queue))

    return "no solution"


print("BFS solution ------->", BFS(start, end))