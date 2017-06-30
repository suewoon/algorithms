#!/usr/bin/env python3 
# solution for https://www.acmicpc.net/problem/1389 

class Game(object):
	class Graph(object):
		def __init__(self,n):
			self.n_of_people = n 
			self.graph = {} #represents relationships 
		
		def add_friend(self,id1,id2):
			if id1 in  self.graph:
				if id2 not in self.graph[id1]:
					self.graph[id1].append(id2)
			else :
				self.graph[id1]=[id2]
		
			if id2 in self.graph:
				if id1 not in self.graph[id2]:
					self.graph[id2].append(id1)
			else :
				self.graph[id2]=[id1] 

	def __init__(self,n):
		self.relationships = self.Graph(n)  
		self.degrees  = [ 0 for i in range(self.relationships.n_of_people) ]

	def get_degrees(self,id1):
		degree=[ 0 for i in range(self.relationships.n_of_people) ]
		to_visit = []
		visited = set()

		to_visit.append(id1)
		visited.add(id1)
		
		depth =0 
		while to_visit :
			person  = to_visit.pop()
			depth+=1 
			for friend in self.relationships.graph[person]:
				if friend not in visited :
					to_visit.append(friend)
					visited.add(friend)
					degree[friend]=1+degree[person]
		
		self.degrees[id1]+=sum(degree)		

if __name__ == '__main__' : 
	(n, m) = tuple(int(x) for x in input().split())
	game = Game(n) # 6 degrees of Kevin Bacon Game ;n : number of users , m : how many relationships with friends 
	for i in range(m):	
		(id1 ,id2) = tuple(int(x) for x in input().split())
		game.relationships.add_friend(id1-1,id2-1)
	
	for i in range(n):
		game.get_degrees(i)
	
	print(game.degrees.index(min(game.degrees))+1)
