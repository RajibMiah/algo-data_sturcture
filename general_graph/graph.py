
class Graph:

    def __init__(self , edges) -> None:
        self.edges = edges
        self.graph_dict = {}

        for start , end in self.edges:
            if start in  self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_path(self , start , end , path =[]):

        path  = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
             return []

        node_path = []

        for node in self.graph_dict[start]:
            if node not in path:
                prev_path_node = self.get_path(node , end , path)
                for p in prev_path_node:
                    node_path.append(p)

        return node_path

    def get_shortest_path(self , start , end):
        all_found_paths = self.get_path(start , end)
        return min(all_found_paths)

            



if __name__ == '__main__':
    routes = [
        ("Mumbai" ,  "Paris"),
        ("Mumbai" , "Dubai"),
        ("Paris" , "Dubai"),
        ("Paris" , "New York"),
        ("Dubai" , "New York"),
        ("New York", "Toranto")
    ]

    start = "Mumbai"
    end = "New York"
    rotuer_graph = Graph(routes)
   

    # print('route' , rotuer_graph.get_path(start , end))
    print('shortest path' , rotuer_graph.get_shortest_path(start , end))
    # print('graph router' , rotuer_graph.graph_dict)