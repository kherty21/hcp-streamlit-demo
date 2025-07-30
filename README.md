
# 💊 Dynamic HCP Targeting & Segmentation

Implement Dynamic HCP Targeting & Segmentation using AI-driven predictive modeling to optimize pharmaceutical marketing efforts. By leveraging machine learning algorithms, the project aims to improve targeting precision, increase sales force efficiency, and enhance marketing ROI. 

This Streamlit app demonstrates an AI-powered dashboard to explore healthcare professional (HCP) data, visualize engagement trends, and predict prescribing lift using a logistic regression model.

---

# Problem Statement
Pharmaceutical field teams and marketers often rely on static HCP segmentation models that fail to account for real-time engagement behavior, changes in prescribing trends, and cross-channel responsiveness. 
As a result:
- Field reps are inefficiently deployed, targeting low-propensity HCPs.
- Marketing campaigns lack the agility to redirect resources toward high-impact channels or prescribers.
- There is limited visibility into predictive indicators of prescribing behavior or disengagement.
These inefficiencies result in suboptimal campaign performance, lost revenue opportunities, and poor return on marketing investments.

---
# Data Sources (Synthetic for PoC)
To simulate real-world pharma data, the PoC will use synthetic datasets representing:
- HCP Profile Data: Specialty, geography, years in practice, patient volume.
- Engagement Metrics: Email opens, rep visits, digital ad clicks, total marketing channel touches.
- Prescribing History: Number of prescriptions historically written for the target brand or category.
- Outcome Variable: Binary flag indicating whether the HCP is likely to prescribe (modeled via logistic regression).


## 🚀 Features

- 📊 Interactive visualizations with Plotly
- 🎛️ Sidebar filters (specialty & engagement score)
- 🧠 Logistic Regression model to predict prescribing lift
- 📥 Download button for filtered data

---

## 📁 File Structure

```
hcp_streamlit_demo_kit/
│
├── hcp_data.csv
├── engagement_data.csv
├── behavioral_data.csv
├── interactive_charts.py
├── requirements.txt
└── README.md
```

---

## 🌐 Deployment on Streamlit Cloud

1. **Create a GitHub Repo**
   - Go to https://github.com and create a new repository (e.g., `hcp-streamlit-demo`)
   - Upload the contents of this project

2. **Sign in to Streamlit Cloud**
   - Visit https://streamlit.io/cloud and sign in with your GitHub account
   - Click **“New App”** and connect your GitHub repository

3. **Set Deployment Settings**
   - **Repository**: `your-username/hcp-streamlit-demo`
   - **Branch**: `main`
   - **Main file path**: `interactive_charts.py`
   - Click **Deploy**

4. **Your app will launch at**:
  (https://hcp-app-demo-bz6wsnvee9fd92s86bbyzx.streamlit.app/)

---

## 🧪 Demo Guide

| Feature | Description |
|--------|-------------|
| 🔍 Filter by Specialty | Select specific specialties from the sidebar |
| 🎯 Predictive Model | Logistic regression scores HCPs for likely prescribing behavior |
| 📊 Engagement Analysis | Explore trends by specialty and digital behaviors |
| 📥 Export CSV | Download filtered results for marketing or sales use |

---

## ⚙️ Local Development

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch app locally
streamlit run interactive_charts.py
```

---

## 📦 Dependencies

- streamlit
- pandas
- numpy
- plotly
- faker
- scikit-learn

---

## 📈 Business Value

- Identify high-potential HCPs
- Prioritize rep outreach based on AI-driven insights
- Optimize omnichannel campaigns with data-backed decisions

---

## 📬 Questions?

Feel free to open an issue or contact Wendy Lawhead for support.
