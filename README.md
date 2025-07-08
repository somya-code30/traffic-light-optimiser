# Traffic Light Timing Optimizer

Smart‑city simulation that adjusts junction green‑light times in real time based on vehicle flow.

## Features
- **Graph model**: Intersections=nodes, roads=directed edges with `flow` (veh/min).
- **Greedy optimiser**: Allocates cycle time in proportion to current flow.
- **Visualiser**: NetworkX + Matplotlib diagram showing flow and green seconds.
- **CLI**:cycle flag to pick a different total cycle length.


## Quick Start
```bash
pip install -r requirements.txt
python traffic_light_optimizer.py
```
## Screenshot
![trafficlight](https://github.com/user-attachments/assets/b17b8d2b-b2dc-4e4b-ac85-a7f65ce93007)

trafficlight.png

## Requirements
networkx>=3.3
matplotlib>=3.9

## Contribution
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.
Fork the repo
Create a feature branch: git checkout -b my‑feature
Commit changes: git commit -m "Add feature"
Push to branch: git push origin my‑feature
Open a PR
