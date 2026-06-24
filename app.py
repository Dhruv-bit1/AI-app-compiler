import streamlit as st
import json
import os

from pipeline.intent_extractor import extract_intent
from pipeline.system_designer import design_system
from pipeline.schema_generator import generate_schema
from pipeline.validator import validate_schema

st.set_page_config(
    page_title="AI App Compiler",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.stButton > button {
    width: 100%;
    height: 3rem;
    border-radius: 12px;
    font-weight: bold;
    font-size: 18px;
}

[data-testid="metric-container"] {
    border: 1px solid rgba(250,250,250,0.2);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}

.block-container {
    padding-top: 1rem;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.title("⚙️ AI Compiler")

    st.markdown("### Prompt Guidelines")

    st.info("""
Include:

✅ Application Name

✅ Features

✅ Roles

✅ Business Rules
""")

    st.markdown("---")

    st.markdown("### Example Prompt")

    st.code("""
Build a Student Management System

Features:
- Student Registration
- Attendance Tracking
- Marks Management

Roles:
- Admin
- Teacher
- Student

Business Rules:
- Teachers update attendance
- Students view marks
""")

# -----------------------------
# HEADER
# -----------------------------

st.markdown("""
# 🚀 AI App Compiler

Transform software requirements into:

✅ Intent Specification

✅ System Architecture

✅ Database Design

✅ API Design

✅ Authentication Schema
""")

st.markdown("---")

# -----------------------------
# INPUT
# -----------------------------

prompt = st.text_area(
    "📝 Describe Your Application",
    height=250,
    placeholder="""
Build a Student Management System

Features:
- Student Registration
- Attendance Tracking
- Marks Management

Roles:
- Admin
- Teacher
- Student

Business Rules:
- Teachers update attendance
- Students can view marks
"""
)

# -----------------------------
# COMPILE
# -----------------------------

if st.button("🚀 Compile Application"):

    if not prompt.strip():
        st.error("Please enter application requirements.")
        st.stop()

    os.makedirs("outputs", exist_ok=True)

    progress = st.progress(0)
    status = st.empty()

    try:

        status.info("🔍 Extracting Intent...")
        intent = extract_intent(prompt)
        progress.progress(33)

        status.info("🏗️ Designing Architecture...")
        design = design_system(intent)
        progress.progress(66)

        status.info("📄 Generating Schema...")
        schema = generate_schema(design)
        progress.progress(100)

        validation = validate_schema(schema)

        if validation["valid"]:
            status.success("✅ Compilation Complete")
        else:
            status.warning("⚠️ Schema Validation Issues Found")

        # -----------------------------
        # SAVE OUTPUTS
        # -----------------------------

        with open("outputs/intent.json", "w") as f:
            json.dump(intent, f, indent=2)

        with open("outputs/design.json", "w") as f:
            json.dump(design, f, indent=2)

        with open("outputs/schema.json", "w") as f:
            json.dump(schema, f, indent=2)

        st.markdown("---")

        # -----------------------------
        # METRICS
        # -----------------------------

        st.subheader("📊 Project Metrics")

        pages = len(design.get("pages", []))
        tables = len(design.get("tables", []))
        apis = len(design.get("apis", []))

        c1, c2, c3 = st.columns(3)

        c1.metric("📄 Pages", pages)
        c2.metric("🗄️ Tables", tables)
        c3.metric("🔌 APIs", apis)

        st.markdown("---")

        # -----------------------------
        # TABS
        # -----------------------------

        tab1, tab2, tab3 = st.tabs([
            "🎯 Intent",
            "🏗️ Architecture",
            "📄 Schema"
        ])

        with tab1:
            st.json(intent)

        with tab2:
            st.json(design)

        with tab3:
            st.json(schema)

        st.markdown("---")

        # -----------------------------
        # DOWNLOADS
        # -----------------------------

        st.subheader("⬇️ Download Artifacts")

        d1, d2, d3 = st.columns(3)

        with d1:
            st.download_button(
                label="Download Intent",
                data=json.dumps(intent, indent=2),
                file_name="intent.json",
                mime="application/json"
            )

        with d2:
            st.download_button(
                label="Download Design",
                data=json.dumps(design, indent=2),
                file_name="design.json",
                mime="application/json"
            )

        with d3:
            st.download_button(
                label="Download Schema",
                data=json.dumps(schema, indent=2),
                file_name="schema.json",
                mime="application/json"
            )

        st.success("📁 All artifacts saved to outputs folder.")

    except Exception as e:
        st.error(f"Error: {str(e)}")