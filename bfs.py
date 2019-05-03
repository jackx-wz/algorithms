#!/usr/local/bin/python
# -*- coding:utf-8 -*-

"""
广度优先算法：
通过广度优先算法，可以找到最短路径
一般用在人际关系，地图路径等
"""

graph = {
    "you":[
        "andi",
        "jack",
        "xdc"
    ],
    "andi":[
        "bob",
        "alice"
    ],
    "xdc":[
        "tom",
        "jone",
        "susan"
    ],
    "bob":[
        "amanda",
        "lily"
    ]
}

ref_map = {}

def bfs_searcg(graph, who, find):
    path = []
    searched = []
    search_queue = []
    search_queue += graph[who]
    ref(who, graph[who])

    while(len(search_queue)):
        name = search_queue.pop()

        if name in searched:
            continue

        if name == find:
            path.append(name)
            while who != ref_map[name]:
                path.append(ref_map[name])
                name = ref_map[name]

            path.append(who)

            return path
        elif (name in graph) and (type(graph[name]) == list):   #当没找到的时候将它的所有关系加到搜索列表中
            search_queue += graph[name]
            ref(name, graph[name])
        else:
            searched.append(name)

    if len(path) == 0:
        return "no path"

def ref(parent, list):
    for name in list:
        if name in ref_map:
            continue
        else:
            ref_map[name] = parent


print(bfs_searcg(graph, 'you', 'susan'))
print(bfs_searcg(graph, 'you', 'amanda'))
print(bfs_searcg(graph, 'you', 'black'))

"""
['susan', 'xdc', 'you']
['amanda', 'bob', 'andi', 'you']
no path
"""