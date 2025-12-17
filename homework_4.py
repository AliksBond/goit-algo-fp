import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def build_heap_tree(heap):
    if not heap:
        return None
    nodes = [Node(val) for val in heap]
    for i in range(len(heap)):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        if left_idx < len(heap):
            nodes[i].left = nodes[left_idx]
        if right_idx < len(heap):
            nodes[i].right = nodes[right_idx]
    return nodes[0]

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

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_r


"""Пояснення що до коду """

Клас Node

Створює вузол бінарного дерева з полями: значення val, лівий/правий нащадки, колір color і унікальний id для ідентифікації.

2️ Функція add_edges

Рекурсивно додає вузли і ребра у граф networkx.

Обчислює координати для відображення вузлів: x горизонтально, y вертикально.

Підключає лівого і правого нащадка до батька через ребра.

3️ Функція draw_tree

Створює направлений граф DiGraph.

Викликає add_edges для побудови структури дерева.

Формує список кольорів і міток для вузлів.

Малює дерево через matplotlib.

4️ Використання

Створюється дерево із заданими вузлами.

Викликається draw_tree(root) для візуалізації у вигляді піраміди.
