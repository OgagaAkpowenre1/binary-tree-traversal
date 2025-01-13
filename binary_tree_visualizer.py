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
def visualize_tree(root, highlight=None):
    if not root:
        return "Tree is empty!"
    graph = graphviz.Digraph()

    def add_nodes_edges(node):
        if not node:
            return
        # Highlight node if it matches the highlight value
        if node.value == highlight:
            graph.node(str(node.value), str(node.value), style="filled", color="red")
        else:
            graph.node(str(node.value), str(node.value))
        if node.left:
            graph.edge(str(node.value), str(node.left.value))
            add_nodes_edges(node.left)
        if node.right:
            graph.edge(str(node.value), str(node.right.value))
            add_nodes_edges(node.right)

    add_nodes_edges(root)
    return graph

# Traversal Helpers
def inorder_traversal(node, result):
    if node:
        inorder_traversal(node.left, result)
        result.append(node.value)
        inorder_traversal(node.right, result)

def preorder_traversal(node, result):
    if node:
        result.append(node.value)
        preorder_traversal(node.left, result)
        preorder_traversal(node.right, result)

def postorder_traversal(node, result):
    if node:
        postorder_traversal(node.left, result)
        postorder_traversal(node.right, result)
        result.append(node.value)

# App UI
st.title("Binary Tree Traversal Visualizer with Animation")

# Tree Input
st.sidebar.header("Tree Input")
nodes = st.sidebar.text_area("Enter node values separated by commas (e.g., 1,2,3,null,null,4,5):")
animation_speed = st.sidebar.slider("Animation Speed (seconds per step)", 0.1, 2.0, 0.5)

if nodes:
    values = [None if v.strip() == "null" else int(v.strip()) for v in nodes.split(",")]
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

    # Traversal Options
    st.subheader("Tree Traversals")
    traversal_type = st.radio("Select Traversal Type", ["Inorder", "Preorder", "Postorder"])
    traversal_result = []
    if traversal_type == "Inorder":
        inorder_traversal(root, traversal_result)
    elif traversal_type == "Preorder":
        preorder_traversal(root, traversal_result)
    elif traversal_type == "Postorder":
        postorder_traversal(root, traversal_result)

    # Animated Traversal
    st.subheader("Animated Traversal")
    traversal_container = st.empty()
    for node_value in traversal_result:
        graph = visualize_tree(root, highlight=node_value)
        traversal_container.graphviz_chart(graph)
        time.sleep(animation_speed)  # Pause for animation

    # Final Traversal Result
    st.write(f"{traversal_type} Traversal Result: {traversal_result}")
