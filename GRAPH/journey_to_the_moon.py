from itertools import chain

class Graph():
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.adj_mat = {key:[] for key in range(n)}

    def add_node(self, a, b):
        self.adj_mat[a].append(b)
        self.adj_mat[b].append(a)

    def dfs(self):
        visited_total = []
        visited_set = set()
        
        def dfs_visit(node, visited):
            if not self.adj_mat[node]: # No neighbors 
                return [node]
            for neighbor in self.adj_mat[node]: 
                if neighbor not in visited:
                    visited.append(neighbor)
                    dfs_visit(neighbor, visited)
            return visited 

        for node in range(self.n):
            if node not in visited_set:
                visited = dfs_visit(node, [])
                visited_total.append(visited)
                visited_set = visited_set.union(set(visited))
      
        print(visited_total) 
        self.comps = [len(comp) for comp in visited_total]
        return

    def get_pairs(self, i):
        pairs = 0
        for idx in range(0, len(self.comps)):
            pairs +=  self.comps[idx]*sum(self.comps[idx+1:])
        return pairs

def main():
    n, p = map(int, input().split())
    graph = Graph(n, p)
    for i in range(p):
        a, b = map(int, input().split())
        graph.add_node(a, b)
    graph.dfs()
    print(graph.get_pairs(0))

if __name__ == '__main__':
    main()
