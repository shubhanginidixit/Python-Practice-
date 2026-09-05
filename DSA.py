import networkx as nx
import matplotlib.pyplot as plt
import time
from openai import OpenAI

# Initialize OpenAI client (replace with your API key)
client = OpenAI(api_key="YOUR_API_KEY_HERE")

# Function to get AI explanation
def ai_explain(step_text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an assistant that explains DSA algorithms step by step."},
                {"role": "user", "content": step_text}
            ]
        )
        return response.choices[0].message.content.strip()
    except:
        return "AI explanation unavailable (check API key or internet)."

# -------------------------------
# 📌 Take user input
# -------------------------------
n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))

edges = []
print("Enter edges in format: u v w (u and v are nodes, w is weight)")
for i in range(m):
    u, v, w = map(int, input(f"Edge {i+1}: ").split())
    edges.append((u, v, w))

# Build graph
G = nx.Graph()
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# Kruskal's Algorithm
sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
parent = {i: i for i in G.nodes}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y)

MST = []
pos = nx.spring_layout(G, seed=42)  # positions for nodes

for u, v, w in sorted_edges:
    step_info = f"Considering edge ({u}, {v}) with weight {w['weight']}..."
    print(step_info)
    explanation = ai_explain(step_info)
    print("AI:", explanation, "\n")

    # Draw graph at this step
    plt.clf()
    edge_colors = []
    for e in G.edges():
        if e in MST or (e[1], e[0]) in MST:
            edge_colors.append("green")
        elif e == (u, v) or e == (v, u):
            edge_colors.append("red")
        else:
            edge_colors.append("gray")

    nx.draw(G, pos, with_labels=True, node_color="pink", edge_color=edge_colors, width=2)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.pause(2)  # wait 2 seconds before next step

    if find(u) != find(v):
        union(u, v)
        MST.append((u, v))
        print("Edge added to MST.\n")
    else:
        print("Edge rejected (forms a cycle).\n")

plt.show()
