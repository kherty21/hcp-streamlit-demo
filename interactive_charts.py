
import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LogisticRegression

# Load Data
@st.cache_data
def load_data():
    hcp = pd.read_csv("hcp_data.csv")
    engagement = pd.read_csv("engagement_data.csv")
    behavioral = pd.read_csv("behavioral_data.csv")
    return hcp.merge(engagement, on="hcp_id").merge(behavioral, on="hcp_id")

df = load_data()

# Generate target variable (simulate prescribing lift)
df["likely_to_prescribe"] = (df["engagement_score"] > 70).astype(int)

# Train a simple logistic regression model
features = ["engagement_score", "rep_visits", "email_open_rate", "click_through_rate", "portal_logins"]
X = df[features]
y = df["likely_to_prescribe"]
model = LogisticRegression()
model.fit(X, y)
df["predicted_lift"] = model.predict_proba(X)[:, 1].round(2)

st.title("HCP Targeting Insights Dashboard")

# Sidebar Filters
specialties = st.sidebar.multiselect("Specialties", options=df["specialty"].unique(), default=list(df["specialty"].unique()))
min_engagement = st.sidebar.slider("Minimum Engagement Score", 0, 100, 30)

filtered_df = df[
    (df["specialty"].isin(specialties)) &
    (df["engagement_score"] >= min_engagement)
]

# Visualization 1
st.subheader("Engagement Score by Specialty")
fig1 = px.box(filtered_df, x="specialty", y="engagement_score", color="specialty")
st.plotly_chart(fig1)

# Visualization 2
st.subheader("Years in Practice vs. Engagement Score")
fig2 = px.scatter(filtered_df, x="years_in_practice", y="engagement_score", color="specialty",
                  size="rep_visits", hover_name="hcp_id")
st.plotly_chart(fig2)

# Visualization 3
st.subheader("Email Open Rate vs Click-through Rate")
fig3 = px.scatter(filtered_df, x="email_open_rate", y="click_through_rate", color="specialty")
st.plotly_chart(fig3)

# Prediction Table
st.subheader("Predicted Prescribing Lift")
st.dataframe(filtered_df[["hcp_id", "specialty", "engagement_score", "predicted_lift"]])

# Data Download
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("Download Filtered Data", data=csv, file_name="filtered_hcp_data.csv", mime="text/csv")
