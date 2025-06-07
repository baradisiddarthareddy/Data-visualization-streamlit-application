import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Enhanced Streamlit App", layout="centered")

st.title("Enhanced Streamlit App with Data Visualization Features")
st.subheader("Upload CSV and Explore Data Visually")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("📄 Uploaded Data", df)

    st.subheader("📈 Summary Statistics")
    st.dataframe(df.describe())

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

    # Feature 1: Pie Chart
    st.subheader("🧩 Pie Chart for Categorical Data")
    pie_col = st.selectbox("Select a categorical column:", categorical_cols)
    if pie_col:
        fig1, ax1 = plt.subplots()
        df[pie_col].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, ax=ax1)
        ax1.set_ylabel('')
        st.pyplot(fig1)

    # Feature 2: Plot between two columns
    st.subheader("📊 Plot Between Two Columns")

    col_x = st.selectbox("Select X-axis column:", numeric_cols)
    col_y = st.selectbox("Select Y-axis column:", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)
    plot_type = st.selectbox("Choose plot type:", ["Line", "Scatter", "Bar"])

    if col_x and col_y:
        fig2, ax2 = plt.subplots()
        if plot_type == "Line":
            ax2.plot(df[col_x], df[col_y])
        elif plot_type == "Scatter":
            ax2.scatter(df[col_x], df[col_y])
        elif plot_type == "Bar":
            ax2.bar(df[col_x], df[col_y])
        ax2.set_xlabel(col_x)
        ax2.set_ylabel(col_y)
        ax2.set_title(f"{plot_type} Plot: {col_x} vs {col_y}")
        st.pyplot(fig2)

    # Feature 3: Correlation Heatmap
    st.subheader("📊 Correlation Heatmap")
    fig3, ax3 = plt.subplots()
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', ax=ax3)
    st.pyplot(fig3)

    # Feature 4: Histogram
    st.subheader("📊 Histogram")
    hist_col = st.selectbox("Select a numeric column to view distribution:", numeric_cols)
    if hist_col:
        fig4, ax4 = plt.subplots()
        ax4.hist(df[hist_col], bins=20, color='skyblue', edgecolor='black')
        ax4.set_title(f"Histogram of {hist_col}")
        st.pyplot(fig4)

# Session state
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0

if st.button("Increment Counter"):
    st.session_state.clicks += 1

st.info(f"🔢 You clicked {st.session_state.clicks} times.")
