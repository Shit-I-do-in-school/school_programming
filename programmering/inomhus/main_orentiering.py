import sys
from heapq import heapify, heappush, heappop

def dijsktra(graph,src,dest):
    inf = sys.maxsize
    node_data = {
    'omr1':{'cost':inf,'pred':[]},
    'omr2':{'cost':inf,'pred':[]},
    'omr3':{'cost':inf,'pred':[]},
    'omr4':{'cost':inf,'pred':[]},
    'omr5':{'cost':inf,'pred':[]},
    'omr6':{'cost':inf,'pred':[]},
    'omr7': {'cost':inf,'pred':[]},
    'omr8': {'cost':inf,'pred':[]}
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
        'omr1':{'omr4': 2, 'omr7': 1},
        'omr2':{'omr3': 3, 'omr4': 1, 'omr5': 2, 'omr6': 2},
        'omr3':{'omr2': 3, 'omr5': 1, 'omr7': 1, 'omr8': 2},
        'omr4':{'omr1': 2, 'omr2': 1, 'omr6': 1},
        'omr5':{'omr2': 2, 'omr3': 1},
        'omr6':{'omr2': 2, 'omr4': 1},
        'omr7':{'omr1': 1, 'omr3': 1},
        'omr8':{'omr3': 2}
    }

    source = 'omr1'
    destination = 'omr8'
    dijsktra(graph,source,destination)