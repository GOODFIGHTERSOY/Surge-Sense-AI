# 🚦 Surge Sense AI Intelligence Hub

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red.svg)
![Hackathon](https://img.shields.io/badge/Flipkart-Gridlock_2.0-yellow.svg)
![Partner](https://img.shields.io/badge/ASTraM-Integration-green.svg)
App:https://surge-sense-ai-ks.streamlit.app/

> **Moving Urban Traffic Management from Reactive Enforcement to Predictive Intelligence.**

Built for **Theme 2: Event-Driven Congestion** of the Flipkart Gridlock Hackathon (in partnership with Bengaluru Traffic Police ASTraM and MapmyIndia).

---

## 🛑 The Operational Challenge
Political rallies, sports events, and sudden public gatherings act as artificial "surge pumps" that inject massive traffic volumes into the city grid. Today, the response is largely reactive:
* Event impact is not mathematically quantified in advance.
* Resource deployment relies heavily on human experience.
* There is no structured post-event learning system.

## 🚀 The Surge Sense AI Solution
Surge Sense AI models the city's road infrastructure not as individual streets, but as a **dynamic graph network**. By treating intersections as nodes and roads as weighted edges, our predictive engine calculates the exact spatial "spillover ripple" of congestion. 

Instead of just predicting traffic, Surge Sense serves as an automated GovTech Command Center, outputting actionable dispatch orders for field personnel hours before a gridlock forms.

---

## ✨ Core Features

### 1. 🌐 Topological Network Forecasting
* Models event locations and simulates traffic surge routing using network edge-weight saturation.
* Calculates exact kinetic spillover radiuses based on event category, expected footfall, and peak-hour overlaps.

### 2. 🤖 Smart Resource Deployment Engine
* Translates mathematical impact scores into tangible logistical requirements.
* Outputs the exact number of traffic personnel and physical barricades required to contain the bottleneck.
* Automatically designates outer-cordon diversion nodes.

### 3. 📱 Automated ASTraM Field Dispatch
* **One-Click Comms:** Generates pre-formatted tactical alerts ready to be broadcasted via WhatsApp or Police Radio.
* **VMS Integration:** Drafts high-visibility alert text for active Variable Message Signs (VMS) on city highways.

### 4. 🧠 Post-Event Machine Learning Loop
* Solves the critical lack of historical adaptability.
* Allows commanders to log ground-truth data post-event.
* The system actively adjusts baseline graph edge-weights to correct historical biases for future predictions.

---

## 🛠️ Technology Stack
* **Frontend/Dashboard:** Streamlit (Custom Dark-Themed UI)
* **Geospatial Rendering:** Folium / Mappls (MapmyIndia) Web SDK
* **Data Processing & Analytics:** Pandas, NumPy
* **Core Logic:** Heuristic Graph Saturation Modeling

---

## 💻 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GOODFIGHTERSOY/Surge-Sense-AI.git
2. **Install the required dependencies:**
    pip install -r requirements.txt
3. **Launch the Intelligence Dashboard:**
    python -m streamlit run app.py



