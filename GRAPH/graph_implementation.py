#/usr/bin/env/python3! 
# various types of graph implementation

"""
ADJACENCY SET REPRESENTATION
Vertices & Neighbors
"""
def make_graph_1():
    a, b, c, d, e, f, g, h = range(8)
    N = [
        {b, c, d, e, f},  #a
        {c, e},  #b
        {d},  #c
        {e},  #d
        {f},  #e
        {c, g, h}, #f
        {f, h},  #g 
        {f, g},  #h
    ]
    print('b is neighbor of a?: {}'.format(b in N[a]))
    print('Degree of vertex F: {}'.format(len(N[f])))

"""
ADJACENCY LISTS
VERTICES & NEIGHBORS
"""
def make_graph_2():
    a, b, c, d, e, f, g, h = range(8)
    N = [
        [b, c, d, e, f], #a
        [c, e], #b
        [d],    #c
        [e],    #d
        [f],    #e
        [c, g, h],  #f
        [f, h], #g
        [f, g]  #h
    ]

"""
ADJACENCY DICTS WITH EDGE WEIGHTS
"""
def make_graph_3():
    a, b, c, d, e, f, g, h = range(8)
    N = [
        {b:2, c:1, d:3, e:9, f:4},
        {c:4, e:3},
        {d:8},
        {e:7},
        {f:5},
        {c:2, g:2, h:2},
        {f:1, h:6},
        {f:9, g:8}
    ]
    print('b is neighbor of a? :{}'.format(b in N[a]))
    print('Degree of vertex F :{}'.format(len(N[f])))
    print('Edge weight for (a->b) :{}'.format(N[a][b]))

"""
ADJACECNEY MATRIX
"""
def make_graph_4():
    a, b, c, d, e, f, g, h = range(8)
    N = [[0,1,1,1,1,1,0,0], 
         [0,0,1,0,1,0,0,0],
         [0,0,0,1,0,0,0,0], 
         [0,0,0,0,1,0,0,0],
         [0,0,0,0,0,1,0,0],
         [0,0,1,0,0,0,1,1],
         [0,0,0,0,0,1,0,1],
         [0,0,0,0,0,1,1,0]]
    print('b is neighbor of a? :{}'.format(N[a][b]))
    print('Degree of vertex F? :{]'.format(sum(N[f])))

"""
ADJACENCY MATRIX WITH WEIGHTS
"""
def make_graph_5():
    a, b, c, d, e, f, g, h = range(8)
    _ = float('inf')
    W = [[0,2,1,3,9,4,_,_], [_,0,4,_,3,_,_,_], [_,_,0,8,_,_,_,_],
         [_,_,_,0,7,_,_,_], [_,_,_,_,0,5,_,_], [_,_,2,_,_,0,2,2],
         [_,_,_,_,_,1,0,6], [_,_,_,_,_,9,8,0]]
    print('b is neighbor of a? :{}'.format(W[a][b] < float('inf')))
    print('e is neighbor of c? :{}'.format(W[c][e] < float('inf')))
    print('Degree of vertex F :{}'.format(sum(1 for w in W[f] if w <
                                              float('inf')))

