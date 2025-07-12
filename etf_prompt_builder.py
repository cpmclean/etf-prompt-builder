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

persona_options = [
    "All Personas",
    "Tactical Cash Managers",
    "Yield Curve Strategists",
    "Income-First Advisors",
    "Educated End-Investors",
    "Financial Advisors",
    "Institutional Investors",
    "Retail Investors",
    "RIA Firms",
    "ETF Strategists"
]

persona = st.selectbox("Select Audience Persona", persona_options)

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

etf = st.selectbox("Select ETF or Product Name", [
    "TBIL",
    "RBIL",
    "ZTOP",
    "RTHY",
    "XBIL",
    "OBIL"
])

focus = st.text_input("Enter Key Focus or Benefit", "Liquidity and Inflation Protection")

# Generate Prompt
if st.button("Generate Prompt"):
    target = "all personas" if persona == "All Personas" else persona

    base_prompt = ""
    if category == "Marketing Copy":
        base_prompt = f"Write 10 {tone.lower()} headlines for {etf}, targeting {target}, emphasizing {focus}."
    elif category == "Persona Messaging":
        base_prompt = f"Rewrite this message to target {target} in a {tone.lower()} tone: '[Insert message]'"
    elif category == "Content Ideas":
        base_prompt = f"Suggest 10 LinkedIn post ideas for {etf} related to {focus}, tailored for {target}, in a {tone.lower()} style."
    elif category == "Campaign Planning":
        base_prompt = f"Develop a seasonal campaign for {etf} targeting {target}, focused on {focus}, with a {tone.lower()} tone."
    elif category == "Explainers":
        base_prompt = f"Write a clear, {tone.lower()} explainer on how {etf} helps with {focus} for {target}."
    elif category == "Comparisons":
        base_prompt = f"Create a comparison between {etf} and an alternative product, focusing on {focus}, for {target}, using a {tone.lower()} tone."
    elif category == "Visual Content":
        base_prompt = f"Suggest 5 infographic ideas to explain how {etf} helps with {focus}, targeted at {target}, in a {tone.lower()} tone."
    elif category == "Workflow Tools":
        base_prompt = f"Audit the following marketing message for {etf}, targeting {target}, with a focus on {focus}. Use a {tone.lower()} tone. '[Insert message]'"

    st.subheader("Generated Prompt")
    st.code(base_prompt, language='markdown')
    st.button("Copy to Clipboard", on_click=st.write, args=("\n\nCopy this prompt manually (clipboard support via frontend JS workaround)",))
