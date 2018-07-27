def dfs(graph,start_point):
    visited = set()
    stack = [start_point]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
    return visited

def dfs_path(graph,start_point,goal):
    stack = [(start_point,[start_point])]
    while stack:
        (vertex,visited) = stack.pop()
        for next_member in visited - [vertex]:
            if next_member == goal:
                print "Here we are"
                return visited + [next_member]
            else:
                stack.extend(next_member,graph(next_member) - visited)

def bfs(graph,start_point):
    queue = [start_point]
    visited = set()
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
def bfs_path(graph,start_point,goal):
    queue = set()
    queue = [(start_point,[start_point])]
    while queue:
        (vertex,visited) = queue.pop(0)
        for next_member in graph[vertex] - visited:
            if next_member == goal:
                return visited + [next_member]
            else:
                queue.extend((next_member,graph[next_member] - visited))

def main():
    graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
    print("Path is {}".format(dfs(graph, 'A')))

if __name__ == "__main__":
    main()
