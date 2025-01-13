import streamlit as st
import graphviz
import time

# Helper class for Binary Tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Visualization Helper
def visualize_tree(root, visited_nodes=set()):
    graph = graphviz.Digraph()
    def add_nodes_edges(node, visited_nodes):
        if not node:
            return
        node_color = "red" if node.value in visited_nodes else "black"
        graph.node(str(node.value), str(node.value), color=node_color)
        if node.left:
            graph.edge(str(node.value), str(node.left.value))
            add_nodes_edges(node.left, visited_nodes)
        if node.right:
            graph.edge(str(node.value), str(node.right.value))
            add_nodes_edges(node.right, visited_nodes)
    
    add_nodes_edges(root, visited_nodes)
    return graph

# Traversal Helpers
def inorder_traversal(node, result, visited_nodes):
    if node:
        inorder_traversal(node.left, result, visited_nodes)
        visited_nodes.add(node.value)  # Mark node as visited
        result.append(node.value)
        time.sleep(0.5)  # Add delay to visualize traversal
        visited_nodes.remove(node.value)  # Unmark node after visit
        inorder_traversal(node.right, result, visited_nodes)

def preorder_traversal(node, result, visited_nodes):
    if node:
        visited_nodes.add(node.value)
        result.append(node.value)
        time.sleep(0.5)
        visited_nodes.remove(node.value)
        preorder_traversal(node.left, result, visited_nodes)
        preorder_traversal(node.right, result, visited_nodes)

def postorder_traversal(node, result, visited_nodes):
    if node:
        postorder_traversal(node.left, result, visited_nodes)
        postorder_traversal(node.right, result, visited_nodes)
        visited_nodes.add(node.value)
        result.append(node.value)
        time.sleep(0.5)
        visited_nodes.remove(node.value)

# App UI
st.title("Binary Tree Traversal Visualizer")

# Tree Input
st.sidebar.header("Tree Input")
nodes = st.sidebar.text_area("Enter node values separated by commas (e.g., 1,2,3,null,null,4,5):")
if nodes:
    values = [None if v == "null" else int(v) for v in nodes.split(",")]
    root = None
    queue = []
    if values:
        root = TreeNode(values.pop(0))
        queue.append(root)
    while queue and values:
        current = queue.pop(0)
        if values:
            left_value = values.pop(0)
            if left_value is not None:
                current.left = TreeNode(left_value)
                queue.append(current.left)
        if values:
            right_value = values.pop(0)
            if right_value is not None:
                current.right = TreeNode(right_value)
                queue.append(current.right)

    # Tree Visualization
    st.subheader("Binary Tree Structure")
    visited_nodes = set()
    graph = visualize_tree(root, visited_nodes)
    st.graphviz_chart(graph)

    # Traversal Options
    st.subheader("Tree Traversals")
    traversal_type = st.radio("Select Traversal Type", ["Inorder", "Preorder", "Postorder"])
    traversal_result = []

    if traversal_type == "Inorder":
        inorder_traversal(root, traversal_result, visited_nodes)
    elif traversal_type == "Preorder":
        preorder_traversal(root, traversal_result, visited_nodes)
    elif traversal_type == "Postorder":
        postorder_traversal(root, traversal_result, visited_nodes)

    st.write(f"{traversal_type} Traversal Result: {traversal_result}")
