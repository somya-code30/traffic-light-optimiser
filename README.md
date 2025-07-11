#  Traffic Light Optimizer (Real Data + ML)

A smart traffic simulation and optimization app built with **Streamlit** using real-world traffic data. This project models intersections and roads as a graph, predicts vehicle flow using **machine learning**, and dynamically allocates **green signal times** to decongest traffic across the city.

---

##  What It Does

- Upload real or simulated traffic data in CSV format
- Edit and customize the road network interactively
- Predict traffic volume using linear regression (length → volume)
- Calculate and optimize green signal times at each junction
- Visualize traffic flow using network graphs

---

##  Features

✅ Real traffic intersections  
✅ Graph-based road modeling with **NetworkX**  
✅ Machine Learning model for traffic volume prediction  
✅ Interactive UI with **Streamlit** + **data editor**  
✅ Congestion-aware green signal optimizer  
✅ Clean, visual summary of signal timing decisions  

---

##  Demo Screenshot
<img width="1840" height="835" alt="image" src="https://github.com/user-attachments/assets/7a64a034-1ad2-4711-acce-a4a10468fce5" />

---

## Quick Start
```bash
pip install -r requirements.txt
streamlit run app.py
```

##  Dataset Format

The CSV file should look like this:

```csv
Area Name,Road/Intersection Name,length_km,Traffic Volume
Whitefield,Indiranagar,5.2,1200
Indiranagar,MG Road,3.8,850
...
```
## Contribution
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.
Fork the repo
Create a feature branch: git checkout -b my‑feature
Commit changes: git commit -m "Add feature"
Push to branch: git push origin my‑feature
Open a PR


