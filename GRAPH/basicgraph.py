
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 21:19:36 2017

@author: suewoonryu

graph implementation 
"""
import string 
import queue

class Vertex(object):
    def __init__(self, id):
        self.id = id 
        self.edges = []
        self.adj_vertices = []
    
    def add_adj_vertex(self,edge, vertex):
        self.edges.append(edge)
        self.adj_vertices.append(vertex)
    
    def __hash__(self):
        '''
        hashability makes an object usable as a dictionary key & set member 
        '''
        return self.id 
    
    def get_degree(self):
        return len(self.edges)
    
    def __eq__(self, other):
        return self.id == other.id 
    
    def __str__(self):
        return str('Vertex: '+str(self.id))

    def __repr__(self):
        return self.__str__()
    
    def __lt__(self,other):
        return self.id < other.id 

class Edge(object):
    def __init__(self, v1, v2, is_directed, weight): 
        self.v1 = v1 
        self.v2 = v2 
        self.is_directed = is_directed
        self.weight = weight
    
    def __hash__(self):
        '''
        hashability makes an object usable as a dictionary key & set member 
        '''
        return hash(self.v1)+hash(self.v2)
    
    def __eq__(self, other):
        return self.v1.id==other.v1.id and self.v2.id == other.v2.id
    
    def __str__(self):
        return str('Edge: '+str(self.v1)+' - '+str(self.v2)+' Weight: '+str(self.weight))
    
    def __repr__(self):
        return self.__str__()
 
class Graph(object):
    def __init__(self,is_directed):
        self.all_edges = [] # [e1, e2, e3, e4]
        self.all_vertices = {}  # {1:v1, 2:v2, 3:v3, 4:v4}
        self.is_directed = is_directed 
    
    def add_edge(self, id1, id2, weight=0):
        if id1 in self.all_vertices: 
            v1 = self.all_vertices[id1]
        else : 
            v1 = Vertex(id1)
            self.all_vertices[id1] = v1 
        if id2 in self.all_vertices:
            v2 = self.all_vertices[id2]
        else : 
            v2 = Vertex(id2)
            self.all_vertices[id2] = v2 
       
        edge = Edge(v1, v2, self.is_directed, weight)
        self.all_edges.append(edge)
        v1.add_adj_vertex(edge,v2)
        if self.is_directed is False : #when graph is not directed, have to connect on both sides 
            v2.add_adj_vertex(edge, v1)

if __name__ == '__main__' : 
    g = Graph(False)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(1,4)
    
    for vertex in g.all_vertices:
        print(str(g.all_vertices[vertex]))
        for edge in g.all_vertices[vertex].edges :
            print(str(edge))


"""
class Graph(object):
    def __init__(self):
        self.graph = {}
        self.make_test_graph()
    
    def make_test_graph(self):
        all_nodes = []
        for char in string.ascii_uppercase:
            node = char
            all_nodes += node
            self.graph[node] = []
        for i in range(len(all_nodes)):
            for j in range(i+1, i+3):
                if j<len(all_nodes):
                    node1 = all_nodes[i]
                    node2 = all_nodes[j]
                    self.graph[node1] += node2
                    self.graph[node2] += node1


def dfs(self,start_node):
    visited_nodes = set()
        to_visit = queue.Queue(0)
        to_visit.put(start_node)
        while not to_visit.empty():
            next_node = to_visit.get()
            if not visited_nodes.__contains__(next_node):
                print("Reached: ",next_node)
                visited_nodes.add(next_node)
                for neighbor in self.graph[next_node]:
                    to_visit.put(next_node)

if __name__ == "__main__":
    g = Graph()
    start_node = 'A'
    g.dfs(start_node)
"""
