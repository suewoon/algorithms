#!/usr/bin/env python3 
#solution for https://www.acmicpc.net/problem/2606

START_NODE = 1 

class Graph(object):
	def __init__(self,n_of_nodes):
		self.nodes = n_of_nodes 
		self.graph = {} 
	def add_edge(self, id1, id2):
		if id1 in self.graph:
			self.graph[id1].append(id2)
		else :
			self.graph[id1] = [id2] 
		
		if id2 in self.graph: 
			self.graph[id2].append(id1)
		else : 
			self.graph[id2] = [id1] 

def dfs(graph, start_node):
	to_visit = []
	visited = set()

	to_visit.append(start_node)
	visited.add(start_node) 
	
	while to_visit : 
		node = to_visit.pop()
		for neighbor in graph.graph[node]: 
			if neighbor not in visited :
				visited.add(neighbor)
				to_visit.append(neighbor) 
	
	return visited 
	
if __name__ == '__main__' : 
	n_of_computers  = int(input())
	n_of_pairs = int(input()) 
	g = Graph(n_of_computers)
	for i in range(n_of_pairs):
		(id1,id2) = tuple(int(x) for x in input().split())
		g.add_edge(id1,id2) 
	visited = dfs(g,START_NODE)
	print(len(visited)-1)
	


