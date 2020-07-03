
import numpy as np

map = np.loadtxt("map.txt", dtype=str, delimiter=' ')

start = {'city': 'Arad',
         'heuristic': 0}
end = 'Bucharest'


def solution(neighbors, start, end):
    result = []
    for x in neighbors:
        if(start['city'] == x[0]['city'] and end == x[len(x)-1]['city']):
            result.append(x)
    return result


def get_best_cost(a):
    b = []
    for x in a:
        b.append(int(x['heuristic']))
    return min(b)


def get_heuristic_cost(a):
    for x in map:
        if x[0] == a:
            return int(x[3])


def get_best_city(fringe):
    for x in fringe:
        if x['heuristic'] == get_best_cost(fringe):
            return x


def BGFS(start, end):
    fringe = []
    closed = []
    fringe.append(start)
    temp = {}
    paths = []
    while(not fringe == []):
        current = get_best_city(fringe)
        fringe.remove(current)
        if current not in closed:
            closed.append(current['city'])
        if current['city'] == end:
            return solution(paths, start, end)
        else:
            for x in map:
                if x[0] == current['city']:
                    neighbors = [current]
                    if x[1] not in closed:
                        temp = {'city': x[1],
                                'heuristic': get_heuristic_cost(x[1])
                                }
                        fringe.append(temp)
                        neighbors.append(temp)
                        paths.append(neighbors)
            for y in paths:
                if y[len(y)-1]['city'] == current['city']:
                    y.append(temp)
        print("-----fringe-------", fringe)

    return "no solution"


print("BGFS solution ------->", BGFS(start, end))
