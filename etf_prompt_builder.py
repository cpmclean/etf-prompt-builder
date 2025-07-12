import streamlit as st

# App title
st.title("ETF Prompt Builder")
st.markdown("Use this app to generate marketing prompts tailored to your ETF products and personas.")

# Dropdowns for input
category = st.selectbox("Select Prompt Category", [
    "Marketing Copy",
    "Persona Messaging",
    "Content Ideas",
    "Campaign Planning",
    "Explainers",
    "Comparisons",
    "Visual Content",
    "Workflow Tools"
])

persona = st.selectbox("Select Audience Persona", [
    "Tactical Cash Managers",
    "Yield Curve Strategists",
    "Income-First Advisors",
    "Educated End-Investors",
    "Financial Advisors",
    "Institutional Investors",
    "Retail Investors",
    "RIA Firms",
    "ETF Strategists"
])

tone = st.selectbox("Select Tone", [
    "Professional",
    "Punchy",
    "Conversational",
    "Compliance-Friendly",
    "Inspirational",
    "Technical",
    "Educational",
    "Urgent",
    "Playful",
    "Seasonal"
])

etf = st.text_input("Enter ETF or Product Name", "TBIL")
focus = st.text_input("Enter Key Focus or Benefit", "Liquidity and Inflation Protection")

# Generate Prompt
if st.button("Generate Prompt"):
    base_prompt = ""
    if category == "Marketing Copy":
        base_prompt = f"Write 10 {tone.lower()} headlines for {etf}, targeting {persona}, emphasizing {focus}."
    elif category == "Persona Messaging":
        base_prompt = f"Rewrite this message to target {persona} in a {tone.lower()} tone: '[Insert message]'"
    elif category == "Content Ideas":
        base_prompt = f"Suggest 10 LinkedIn post ideas for {etf} related to {focus}, tailored for {persona}, in a {tone.lower()} style."
    elif category == "Campaign Planning":
        base_prompt = f"Develop a seasonal campaign for {etf} targeting {persona}, focused on {focus}, with a {tone.lower()} tone."
    elif category == "Explainers":
        base_prompt = f"Write a clear, {tone.lower()} explainer on how {etf} helps with {focus} for {persona}."
    elif category == "Comparisons":
        base_prompt = f"Create a comparison between {etf} and an alternative product, focusing on {focus}, for {persona}, using a {tone.lower()} tone."
    elif category == "Visual Content":
        base_prompt = f"Suggest 5 infographic ideas to explain how {etf} helps with {focus}, targeted at {persona}, in a {tone.lower()} tone."
    elif category == "Workflow Tools":
        base_prompt = f"Audit the following marketing message for {etf}, targeting {persona}, with a focus on {focus}. Use a {tone.lower()} tone. '[Insert message]'"

    st.subheader("Generated Prompt")
    st.code(base_prompt, language='markdown')
