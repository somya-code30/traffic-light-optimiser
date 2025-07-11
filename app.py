import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title=" Traffic Light Optimizer", layout="wide")
st.title("Traffic Light Optimizer (Real Data)")

st.markdown(
    "Upload real traffic data of roads to **simulate**, **predict**, and **optimize** signal timings "
    "at intersections using machine learning and network flow analysis."
)

# Upload dataset
uploaded = st.file_uploader("upload the CSV file with real traffic data to continue.", type=["csv"])
if not uploaded:
    st.info("Please upload the CSV file with real traffic data to continue.")
    st.stop()

# Load dataset
df = pd.read_csv(uploaded)
st.success("Dataset uploaded successfully!")
st.dataframe(df.head(), use_container_width=True)

# Road Editor Interface
st.subheader("Define or Edit Road Network")
default_roads = [
    {"from": row["Area Name"], "to": row["Road/Intersection Name"], "length_km": row["length_km"]}
    for _, row in df.head(5).iterrows()
]
roads = st.data_editor(default_roads, num_rows="dynamic", use_container_width=True)

# Build Graph
G = nx.DiGraph()
flows = {}

for road in roads:
    u, v, l = road["from"], road["to"], road["length_km"]
    match = df[(df["Area Name"] == u) & (df["Road/Intersection Name"] == v)]
    flow = int(match["Traffic Volume"].values[0]) if not match.empty else np.random.randint(200, 1000)
    G.add_edge(u, v, length_km=l, flow=flow)
    flows[(u, v)] = flow

# ML-based Flow Prediction (Optional)
if "length_km" in df.columns and "Traffic Volume" in df.columns:
    st.subheader("ML Model: Predict Flow from Road Length")
    X = df[["length_km"]]
    y = df["Traffic Volume"]
    model = LinearRegression()
    model.fit(X, y)
    st.info(f"Model: flow = {model.coef_[0]:.2f} × length + {model.intercept_:.2f}")

    for u, v in G.edges:
        predicted_flow = model.predict([[G[u][v]["length_km"]]])[0]
        G[u][v]["flow"] = int(predicted_flow)
        flows[(u, v)] = int(predicted_flow)

# Signal Timing Optimization
st.subheader(" Signal Timing Optimization")

cycle = st.slider("Total Green Signal Cycle Time (in seconds)", 30, 180, 90, step=10)
timings = {}

for node in G.nodes:
    incoming_edges = list(G.in_edges(node, data=True))
    if not incoming_edges:
        continue
    total_flow = sum(data["flow"] for _, _, data in incoming_edges)
    node_timings = {}
    for u, v, data in incoming_edges:
        green_time = max(5, (data["flow"] / total_flow) * cycle)
        node_timings[(u, v)] = round(green_time, 1)
    timings[node] = node_timings

# Display Green Timings
st.subheader(" Optimized Signal Timings")
for node, node_timings in timings.items():
    st.markdown(f"### 🚥 Intersection: {node}")
    for (u, _), green in node_timings.items():
        st.write(f"• From **{u}** ➝ green for **{green} seconds** (Flow: {flows[(u, _)]} vehicles)")

# Graph Visualization
st.subheader("Road Network Visualization")
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=800, node_color='lightgreen', font_size=10)
nx.draw_networkx_edge_labels(
    G, pos, edge_labels={(u, v): f"{flows[(u, v)]}" for u, v in G.edges}, font_color='red'
)
st.pyplot(plt.gcf())
plt.clf()
