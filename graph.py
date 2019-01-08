import random
import json


class Node:
    def __init__(self, id_nr):
        self.id_nr = id_nr
        self.passengers = 0
        self.adj_list = []

    def has_passengers(self):
        if self.passengers > 0:
            return True
        return False

    def create_passenger(self):
        self.passengers += 1

    def add_edge(self, other, weight):
        self.adj_list.append((other, weight))

    def is_edge_adj(self, other):
        nodes = set()
        for edge in self.adj_list:
            nodes.add(edge[0])
        if other in nodes:
            return True
        return False

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


def count_edges(graph):
    edges = []
    for node in graph:
        for edge in node.adj_list:
            edges.append(edge)
    return len(edges) / 2


def random_add_edges(graph, edges, max_weight):
    while edges > 0:
        index_1 = random.randint(0, len(graph) - 1)
        index_2 = random.randint(0, len(graph) - 1)
        while index_2 == index_1 or graph[index_1].is_edge_adj(graph[index_2].id_nr):
            index_1 = random.randint(0, len(graph) - 1)
            index_2 = random.randint(0, len(graph) - 1)
        weight = random.randint(1, max_weight)
        graph[index_1].add_edge(graph[index_2].id_nr, weight)
        graph[index_2].add_edge(graph[index_1].id_nr, weight)
        edges -= 1
    return graph


def generate_graph(vertices, edges, max_weight):
    current_id = 0
    graph = set()

    # Create all the vertices of the graph
    for i in range(vertices):
        graph.add(Node(current_id))
        current_id += 1

    # Generate a spanning tree
    S, T = graph, set()
    current_node = random.sample(S, 1).pop()
    S.remove(current_node)
    T.add(current_node)
    while S:
        new_node = random.sample(S, 1).pop()
        S.remove(new_node)
        weight = random.randint(1, max_weight)
        current_node.add_edge(new_node.id_nr, weight)
        new_node.add_edge(current_node.id_nr, weight)
        T.add(new_node)
        current_node = new_node

    edges = edges - (vertices - 1)
    graph = list(T)

    return random_add_edges(graph, edges, max_weight)


def output_graph(graph):
    dictionary = {}
    for node in graph:
        dictionary[node.id_nr] = {"id": node.id_nr, "passengers": node.passengers,
                                  "adj_list": node.adj_list}
    with open("graph.json", "w") as write_file:
        json.dump(dictionary, write_file)


def dict_to_array(graph_dictionary):
    graph = []
    for key in graph_dictionary.keys():
        id_nr = graph_dictionary[key]["id"]
        passengers = graph_dictionary[key]["passengers"]
        adj_list = graph_dictionary[key]["adj_list"]
        node = Node(id_nr=id_nr)
        node.passengers = passengers
        node.adj_list = adj_list
        graph.append(node)
    return graph


def read_graph(path_file):
    with open(path_file) as data_file:
        data_loaded = json.load(data_file)
    return dict_to_array(data_loaded)


def node_amount(vertices, edges):
    if edges > vertices*(vertices-1)/2:
        raise ValueError("Number of edges can not exceed nr_vertices(nr_vertices-1)/2")
    elif edges < vertices - 1:
        raise ValueError("Number of edges can not be smaller than nr_vertices-1")
    elif vertices < 2:
        raise ValueError("Number of vertices can not be less than 2")


def validate(vertices, edges):
    try:
        node_amount(vertices, edges)
    except ValueError as e:
        print("Caught error:", repr(e))


def main():
    # temp = generate_graph(5, 10, 20)
    # output_graph(temp)
    # read_graph("graph.json")
    # validate(10, 2)
    # validate(10, 2000)
    # validate(1,0)
    # validate(5,5)
    pass


if __name__ == "__main__":
    main()
