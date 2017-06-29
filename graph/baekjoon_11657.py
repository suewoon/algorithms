#!/usr/bin/env python3 
# solution for https://www.acmicpc.net/problem/11657

class Timemachine(object):	
 
	class Graph(object):
		def __init__(self,n,m):
			self.n = n # number of cities 
			self.m = m # number of buses connecting between two cities 
			self.graph = {} # directed graph  

		def add_edge(self,id1,id2,time):
		# it takes 'time' to go from 'id1' to 'id2' 
			if id1 in self.graph: 
				self.graph[id1].append((id2,time))
			else :
				self.graph[id1] = [(id2,time)] 
	
	START_NODE = 1 

	def __init__(self,n,m):
		self.city_map=self.Graph(n,m)
		
	def initialize(self):
		n = self.city_map.n 
		self.d = [ float('inf') for i in range(n) ]
		self.d[0] = 0

	def relax(self,u,v):
		id1 = u ; id2 =v[0] ; time=v[1] 
		if self.d[id2] > self.d[id1] + time : 
			self.d[id2] = self.d[id1] + time 
	
	def get_min_time(self):
		self.initialize()

		#bellman-ford algorithm 
		n = self.city_map.n
		for i in range(n-1):
			for u in self.city_map.graph:
				for v in city_map.graph[u]:
					self.relax(u,v)

		#negative-cycle check
		for u in city_map.graph:
			for v in city_map.graph[u]:
				node = v[0]
				time = v[1]
				if not self.d[node] <= self.d[u]+time :
					self.d[node]=-1
					break 
	

if __name__ == '__main__' : 
	(n,m) = tuple(int(x) for x in input().split()) 
	timemachine = Timemachine(n,m)
	city_map = timemachine.city_map

	for i in range(m):
		(id1, id2, time) = tuple(int(x) for x in input().split()) 
		city_map.add_edge(id1-1,id2-1,time) 

	timemachine.get_min_time()
	min_time_list = timemachine.d
	print(min_time_list)
