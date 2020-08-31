#
# graph= {
#     "A":["B", "C"],
#     "B":["D", "E"],
#     "C":["F"],
#     "D":[],
#     "E":["F"],
#     "F":[],
#
# }
#
#
# def dfs(visit, graph, node):
#     if node not in visit:
#         print(node)
#         visit.add(node)
#         for neighbour in graph[node]:
#             dfs(visit, graph, neighbour)
#
#
# if __name__ == "__main__":
#     visited = set()
#     dfs(visited, graph, "A")


class Node:

    def __init__(self, node_id):
        self.id = node_id
        self.children = []

    def __str__(self):
        return f"Node: {self.id}"

    def __repr__(self):
        return str(self)

    @staticmethod
    def search(start_node, node_id):
        """
        Tree traversing
        :param start_node: root - object without a parent
        :param node_id: object we are looking for
        :return: List of objects traversed
        """
        visited = []
        stack = [start_node, ]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)

            if node.id == node_id:
                return visited

            for child in node.children:
                stack.append(child)


if __name__ == "__main__":
    root = Node("Mieszko I")
    n1 = Node("Bolesław Chrobry")
    root.children.append(n1)

    n2 = Node("Mieszko II")
    n1.children.append(n2)

    n3 = Node("Kazimierz Odnowiciel")
    n2.children.append(n3)

    n4 = Node("Bolesław Smiały")
    n5 = Node("Władysław Herman")
    n3.children = [n4, n5]

    n6 = Node("Zbigniew")
    n7 = Node("bolesław Krzywousty")
    n5.children = [n6, n7]

    print(Node.search(root, "Zbigniew"))
