#!/usr/local/bin/python
# -*- coding:utf-8 -*-

graph = {
    'start': {
        'a': 6,
        'b': 2
    },
    'a': {
        'fin': 1
    },
    'b': {
        'a': 3,
        'fin': 5
    },
    'fin': {}
}

infinity = float('inf')
costs = {
    'a': 6,
    'b': 2,
    'fin': infinity
}
parents = {
    'a': 'start',
    'b': 'start',
    'fin': None
}
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if (node not in processed) and (cost < lowest_cost):
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node

def dijkstra(graph, costs, parents):
    node = find_lowest_cost_node(costs)

    while node is not  None:
        cost = costs[node]
        neighbors = graph[node]

        for n in neighbors.keys():
            new_cost = cost + neighbors[n]

            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

    return (costs['fin'], parents)

print dijkstra(graph, costs, parents)

