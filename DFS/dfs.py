
def dfs(visited , graph , node):
    if node is not visited:
        print(node)
        visited.add(node)
        for node in graph[node]:
            dfs(visited , graph , node)
    
if __name__ == "__main__":
    graph = {
        '5' : ['3','7'],
        '3' : ['2', '4'],
        '7' : ['8'],
        '2' : [],
        '4' : ['8'],
        '8' : []
    }

    visited = set()
    dfs(visited , graph , '5')

   