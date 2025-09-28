import streamlit as st
import pandas as pd
from rewrite_logic import rewrite_query  # import your function from notebook
from evaluation import evaluate_query


# Sidebar content
st.sidebar.title("About This Project")
st.sidebar.markdown("""
This tool rewrites user queries based on personalization fields like location, interests, and device.  
It supports multiple rewrite strategies and evaluates output quality using ROUGE and BERTScore.
""")


st.title("🎯 Personalized Query Rewriter")

# Input fields
original_query = st.text_input("Original Query")
rewrite_type = st.selectbox("Rewrite Type", [
    "formalization", "elaboration", "simplification",
    "formalization + localization", "elaboration + localization", "simplification + localization"
])
location = st.text_input("Location")
interests = st.text_input("Interests")
device = st.text_input("Device")
user_profile = st.text_input("User Profile")

# Dataset preview
df = pd.read_csv("synthetic_queries_dataset.csv")
st.subheader("📁 Sample Dataset")
st.dataframe(df.head(5))


if st.button("Generate Rewrite"):
    rewritten = rewrite_query(original_query, rewrite_type, location, interests, device, user_profile)
    st.write("🔁 Rewritten Query:")
    st.success(rewritten)

    # Debug print
    print("Evaluating:", original_query, rewritten)

    # Evaluation scores
    rouge1, rougeL, bert = evaluate_query(original_query, rewritten)
    st.subheader("📊 Evaluation Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("ROUGE-1", f"{rouge1:.2f}")
    col2.metric("ROUGE-L", f"{rougeL:.2f}")
    col3.metric("BERTScore", f"{bert:.2f}")