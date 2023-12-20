import sys
from heapq import heapify, heappush, heappop

def dijsktra(graph,src,dest):
    inf = sys.maxsize
    node_data = {
    'A':{'cost':inf,'pred':[]},
    'B':{'cost':inf,'pred':[]},
    'C':{'cost':inf,'pred':[]},
    'D':{'cost':inf,'pred':[]},
    'E':{'cost':inf,'pred':[]},
    'F':{'cost':inf,'pred':[]},
    'G': {'cost':inf,'pred':[]},
    'H': {'cost':inf,'pred':[]}
    }
    node_data[src]['cost'] = 0
    visited = []
    temp = src
    for i in range(5):
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:
                if j not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + [temp]
                    heappush(min_heap,(node_data[j]['cost'],j))
        heapify(min_heap)
        temp = min_heap[0][1]
    print("Shortest Distance: " + str(node_data[dest]['cost']))
    print("Shortest Path: " + str(node_data[dest]['pred'] + list(dest)))


if __name__ == "__main__":
    graph = {
        'A':{'D': 2, 'G': 1},
        'B':{'C': 3, 'D': 1, 'E': 2, 'F': 2},
        'C':{'B': 3, 'E': 1, 'G': 1, 'H': 2},
        'D':{'A': 2, 'B': 1, 'F': 1},
        'E':{'B': 2, 'C': 1},
        'F':{'B': 2, 'D': 1},
        'G':{'A': 1, 'C': 1},
        'H':{'C': 2}
    }

    source = 'B'
    destination = 'G'
    dijsktra(graph,source,destination)