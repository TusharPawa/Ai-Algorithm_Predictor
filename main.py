import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from pycaret.classification import setup as cls_setup, compare_models as cls_compare, pull as cls_pull, save_model as cls_save
from pycaret.regression import setup as reg_setup, compare_models as reg_compare, pull as reg_pull, save_model as reg_save
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport

# Initialize session state
if 'df' not in st.session_state:
    st.session_state.df = None
if 'problem_type' not in st.session_state:
    st.session_state.problem_type = None
if 'chosen_target' not in st.session_state:
    st.session_state.chosen_target = None
if 'best_model_df' not in st.session_state:
    st.session_state.best_model_df = None

# Dashboard Layout
st.set_page_config(layout="wide", page_title="AutoML Dashboard", page_icon="📊")
st.markdown("""
    <style>
    .main {background-color: #1e1e1e; padding: 20px; border-radius: 10px; color: white;}
    .stButton>button { width: 100%; }
    .sidebar .block-container { background-color: #252526; }
    .css-1aumxhk { background-color: #252526; }
    .css-145kmo2 { color: white; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png", use_column_width=True)
st.sidebar.title("Dashboard Navigation")
choice = st.sidebar.radio("Select Option", ["Upload", "Profiling", "Data Cleaning", "Modelling", "Best Algorithm", "Download"])
st.sidebar.info("Automate Data Processing & Model Training with Ease.")

st.title("📊 AutoML Dashboard")

# Upload Section
if choice == "Upload":
    st.subheader("Upload Your Dataset")
    file = st.file_uploader("Upload Your Dataset", type=["csv"])
    if file is not None:
        st.session_state.df = pd.read_csv(file)
        st.session_state.df.to_csv("dataset.csv", index=False)
        st.dataframe(st.session_state.df)

if os.path.exists("dataset.csv") and st.session_state.df is None:
    st.session_state.df = pd.read_csv("dataset.csv")

df = st.session_state.df

# Profiling Section
if choice == "Profiling":
    if df is not None and not df.empty:
        st.subheader("Exploratory Data Analysis")
        profile = ProfileReport(df, explorative=True)
        st_profile_report(profile)
    else:
        st.error("Please upload a dataset first.")

# Data Cleaning Section
if choice == "Data Cleaning":
    if df is not None and not df.empty:
        st.subheader("Data Cleaning")
        missing_values = df.isnull().sum()
        st.write("### Missing Values in Dataset")
        st.write(missing_values[missing_values > 0])
        
        if missing_values.sum() > 0:
            column_to_clean = st.selectbox("Select column to clean", df.columns[df.isnull().any()])
            strategy = st.radio("Select imputation strategy", ["Mean", "Median", "Mode"])
            
            if st.button("Apply Cleaning"):
                if strategy == "Mean":
                    imputer = SimpleImputer(strategy='mean')
                elif strategy == "Median":
                    imputer = SimpleImputer(strategy='median')
                else:
                    imputer = SimpleImputer(strategy='most_frequent')
                
                df[column_to_clean] = imputer.fit_transform(df[[column_to_clean]])
                st.session_state.df = df
                st.success(f"Missing values in {column_to_clean} filled using {strategy} strategy.")
                st.dataframe(st.session_state.df)
    else:
        st.error("Please upload a dataset first.")

# Modelling Section
if choice == "Modelling":
    if df is not None and not df.empty:
        st.subheader("Model Training")
        st.session_state.chosen_target = st.selectbox("Choose the Target Column", df.columns)
        st.session_state.problem_type = st.radio("Select Problem Type", ["Classification", "Regression"])

        if st.button("Run Modelling"):
            if st.session_state.problem_type == "Classification":
                cls_setup(df, target=st.session_state.chosen_target, verbose=False)
                best_model = cls_compare()
                st.session_state.best_model_df = cls_pull()
                cls_save(best_model, "best_model")
            else:
                reg_setup(df, target=st.session_state.chosen_target, verbose=False)
                best_model = reg_compare()
                st.session_state.best_model_df = reg_pull()
                reg_save(best_model, "best_model")
    else:
        st.error("Please upload a dataset first.")

# Best Algorithm Section
if choice == "Best Algorithm":
    if st.session_state.best_model_df is not None:
        st.subheader("Best Algorithm Performance")
        best_model_df = st.session_state.best_model_df
        best_model = best_model_df.iloc[0]  # Get the best model row
        
        st.write(f"### Best Model: {best_model[0]}")
        st.write(f"#### Training Accuracy: {best_model[1]}")
        st.write(f"#### Testing Accuracy: {best_model[2]}")
        
        st.write("### Comparison Table")
        st.dataframe(best_model_df)
        
        st.write("### Training & Testing Score Comparison")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x=best_model_df.iloc[:, 0], y=best_model_df.iloc[:, 1], color='blue', label='Training Score')
        sns.barplot(x=best_model_df.iloc[:, 0], y=best_model_df.iloc[:, 2], color='red', alpha=0.6, label='Testing Score')
        ax.set_xlabel("Algorithms")
        ax.set_ylabel("Score")
        ax.set_title("Training vs Testing Score Comparison")
        ax.set_xticklabels(best_model_df.iloc[:, 0], rotation=45)
        ax.legend()
        st.pyplot(fig)
    else:
        st.error("No model found. Please run the modelling step first.")
