import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from fuzzy_engine import build_system
from explainability import explain

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="AI HR Dashboard",
    page_icon="🤖",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.main {
    background-color: #0f1117;
}

.metric-card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: white;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
}

.top-box {
    background-color: #16213E;
    padding: 25px;
    border-radius: 15px;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# TITLE
# =====================================

st.title("🤖 AI-Powered HR Decision Dashboard")

st.markdown("""
Professional Fuzzy Logic Based Recruitment & Candidate Ranking System
""")

# =====================================
# BUILD SYSTEM
# =====================================

sim = build_system()

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("📂 HR Analytics Panel")

file = st.sidebar.file_uploader(
    "Upload Candidate CSV",
    type=["csv"]
)

st.sidebar.markdown("---")

st.sidebar.subheader("🎯 Filters")

min_score = st.sidebar.slider(
    "Minimum Score",
    0,
    100,
    50
)

selected_category = st.sidebar.multiselect(
    "Candidate Categories",
    ["Reject", "Risky", "Good", "Excellent"],
    default=["Reject", "Risky", "Good", "Excellent"]
)

# =====================================
# CATEGORY SYSTEM
# =====================================

def get_category(score):

    if score < 40:
        return "Reject"

    elif score < 60:
        return "Risky"

    elif score < 80:
        return "Good"

    else:
        return "Excellent"

# =====================================
# COLOR SYSTEM
# =====================================

def score_color(score):

    if score < 40:
        return "🔴"

    elif score < 60:
        return "🟠"

    elif score < 80:
        return "🟡"

    else:
        return "🟢"

# =====================================
# MAIN SYSTEM
# =====================================

if file:

    df = pd.read_csv(file)

    scores = []
    explanations = []
    categories = []
    colors = []

    # =====================================
    # FUZZY ANALYSIS
    # =====================================

    for _, row in df.iterrows():

        sim.input['gpa'] = row['gpa']
        sim.input['experience'] = row['experience']
        sim.input['projects'] = row['projects']
        sim.input['test_score'] = row['test_score']
        sim.input['communication'] = row['communication']

        try:

            sim.compute()

            if 'suitability' in sim.output:
                score = sim.output['suitability']
            else:
                score = 50

        except:
            score = 50

        scores.append(score)

        explanations.append(explain(row))

        category = get_category(score)

        categories.append(category)

        colors.append(score_color(score))

    # =====================================
    # RESULTS
    # =====================================

    df["Score"] = scores
    df["Category"] = categories
    df["Status"] = colors

    # FILTERS

    df = df[df["Score"] >= min_score]

    df = df[df["Category"].isin(selected_category)]

    df = df.sort_values("Score", ascending=False)

    # =====================================
    # KPI SECTION
    # =====================================

    avg_score = round(df["Score"].mean(), 2)

    top_score = round(df["Score"].max(), 2)

    total_candidates = len(df)

    excellent_count = len(df[df["Category"] == "Excellent"])

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
        <h2>👥 Candidates</h2>
        <h1>{total_candidates}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
        <h2>📈 Avg Score</h2>
        <h1>{avg_score}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
        <h2>🏆 Top Score</h2>
        <h1>{top_score}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card">
        <h2>⭐ Excellent</h2>
        <h1>{excellent_count}</h1>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # =====================================
    # TOP CANDIDATE PANEL
    # =====================================

    top_candidate = df.iloc[0]

    st.markdown(f"""
    <div class="top-box">
    <h2>🏆 Top Candidate Recommendation</h2>

    <h3>Score: {top_candidate['Score']:.2f}</h3>

    <h3>Category: {top_candidate['Category']}</h3>

    <p>
    This candidate demonstrates the strongest overall suitability
    according to the fuzzy decision system.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # =====================================
    # TABLE
    # =====================================

    st.subheader("📋 Candidate Ranking")

    st.dataframe(df)

    # =====================================
    # DOWNLOAD BUTTON
    # =====================================

    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "⬇ Download Analyzed Results",
        csv,
        "analyzed_candidates.csv",
        "text/csv"
    )

    st.markdown("---")

    # =====================================
    # CHARTS
    # =====================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📊 Score Distribution")

        fig, ax = plt.subplots()

        ax.hist(df["Score"], bins=10)

        st.pyplot(fig)

    with col2:

        st.subheader("📈 Category Distribution")

        category_counts = df["Category"].value_counts()

        fig2, ax2 = plt.subplots()

        ax2.pie(
            category_counts,
            labels=category_counts.index,
            autopct='%1.1f%%'
        )

        st.pyplot(fig2)

    st.markdown("---")

    # =====================================
    # INTERACTIVE EXPLAINABILITY
    # =====================================

    st.subheader("🧠 Candidate AI Analysis")

    selected_index = st.selectbox(
        "Select Candidate",
        df.index
    )

    selected_row = df.loc[selected_index]

    st.write("### Candidate Information")

    st.write(selected_row)

    st.write("### Candidate Score")

    st.progress(int(selected_row["Score"]))

    st.write(f"Suitability Score: {selected_row['Score']:.2f}")

    st.write("### AI Explanation")

    for e in explain(selected_row):
        st.info(e)

    st.success("Analysis Completed Successfully!")

# =====================================
# EMPTY PAGE
# =====================================

else:

    st.info("📂 Please upload a CSV dataset to start HR analysis.")