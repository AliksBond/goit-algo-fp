import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="#1F77B4"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(graph, pos):
    colors = [node[1]['color'] for node in graph.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in graph.nodes(data=True)}
    plt.figure(figsize=(10, 6))
    nx.draw(graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def generate_color(index, total):
    intensity = int(255 * index / total)
    return f"#{intensity:02X}{intensity:02X}{255-intensity:02X}"

def dfs_visualization(root):
    if root is None:
        return
    graph = nx.DiGraph()
    pos = {root.id: (0,0)}
    add_edges(graph, root, pos)
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            node.color = generate_color(len(visited), len(graph.nodes()))
            draw_tree(graph, pos)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def bfs_visualization(root):
    if root is None:
        return
    graph = nx.DiGraph()
    pos = {root.id: (0,0)}
    add_edges(graph, root, pos)
    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            node.color = generate_color(len(visited), len(graph.nodes()))
            draw_tree(graph, pos)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

dfs_visualization(root)

for node in [root, root.left, root.left.left, root.left.right, root.right, root.right.left]:
    node.color = "#1F77B4"

bfs_visualization(root)
