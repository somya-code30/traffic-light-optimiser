# traffic_light_optimizer.py
"""
Traffic Light Timing Optimizer
--------------------------------
Smart‑city simulation that adjusts each junction’s green‑light durations in real time
based on live or simulated vehicle flow.

DSA Concepts: Graphs · BFS · Greedy Algorithms
"""

from __future__ import annotations
import argparse
import random
from typing import Dict, Tuple

import networkx as nx
import matplotlib.pyplot as plt


def build_sample_graph(seed: int = 42) -> nx.DiGraph:
    """Create a small directed graph with random vehicle flows."""
    random.seed(seed)
    G = nx.DiGraph()
    intersections = ["A", "B", "C", "D"]
    G.add_nodes_from(intersections)
    roads = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"),
             ("A", "C"), ("B", "D")]
    for u, v in roads:
        G.add_edge(u, v, flow=random.randint(10, 60))
    return G


def optimise_timings(G: nx.DiGraph, cycle_time: int = 90,
                     min_green: int = 5, max_green: int = 60) -> Dict[str, Dict[Tuple[str, str], float]]:
    """Allocate green‑times greedily proportional to flow."""
    timings: Dict[str, Dict[Tuple[str, str], float]] = {}
    for node in G.nodes:
        incoming = list(G.in_edges(node, data="flow"))
        if not incoming:
            continue
        total = sum(flow for *_, flow in incoming) or 1
        node_times = {}
        for u, v, flow in incoming:
            green = max(min_green, (flow / total) * cycle_time)
            green = min(green, max_green)
            node_times[(u, v)] = round(green, 1)
        timings[node] = node_times
    return timings


def draw_network(G: nx.DiGraph, timings) -> None:
    pos = nx.spring_layout(G, seed=7)
    flows = [G[u][v]['flow'] for u, v in G.edges]
    widths = [0.1 + f / 10 for f in flows]
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightgrey')
    nx.draw_networkx_labels(G, pos, font_weight='bold')
    nx.draw_networkx_edges(G, pos, width=widths, arrowsize=20, arrowstyle='->')
    for (u, v, data) in G.edges(data=True):
        x, y = (pos[u] + pos[v]) / 2
        flow = data['flow']
        green = timings.get(v, {}).get((u, v))
        label = f"{flow}veh/m\n{green}s" if green else f"{flow}veh/m"
        plt.text(x, y, label, fontsize=8, ha='center', va='center')
    plt.title("Traffic Flow and Optimised Green Times") 
    plt.axis('off')
    plt.tight_layout()
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Traffic Light Timing Optimizer")
    parser.add_argument("--cycle", type=int, default=90, help="Cycle time in seconds") 
    args = parser.parse_args()
    G = build_sample_graph()
    timings = optimise_timings(G, cycle_time=args.cycle)
    draw_network(G, timings)
    for node, t in timings.items():
        print(f"\nIntersection {node} (cycle {args.cycle}s):")
        for (u, _), g in t.items():
            print(f"  Approach from {u}: {g}s")


if __name__ == "__main__":
    main()
