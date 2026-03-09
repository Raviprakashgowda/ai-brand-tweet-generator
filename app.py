import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
from prompts import brand_analysis_prompt, tweet_generation_prompt

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Check API key
if not api_key:
    st.error("❌ GROQ_API_KEY not found. Please add it to your .env file.")
    st.stop()

# Initialize Groq client
client = Groq(api_key=api_key)

# Streamlit UI
st.set_page_config(page_title="AI Brand Tweet Generator", page_icon="🐦")

st.title("🐦 AI Brand Tweet Generator")
st.write("Generate **10 on-brand tweets** using AI based on brand voice.")

st.divider()

# Input fields
brand = st.text_input("Brand Name")

industry = st.text_input("Industry / Category")

objective = st.selectbox(
    "Campaign Objective",
    ["Engagement", "Promotion", "Awareness"]
)

product = st.text_area("Describe the brand / product")

generate = st.button("Generate Tweets")

st.divider()

# Generate tweets
if generate:

    if brand.strip() == "" or product.strip() == "":
        st.warning("Please enter at least the brand name and product description.")
        st.stop()

    # -------- Brand Voice Analysis --------
    with st.spinner("Analyzing brand voice..."):

        analysis_prompt = brand_analysis_prompt(
            brand,
            industry,
            product,
            objective
        )

        analysis_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": analysis_prompt}
            ]
        )

        brand_voice = analysis_response.choices[0].message.content

    st.subheader("🧠 Brand Voice Analysis")
    st.write(brand_voice)

    st.divider()

    # -------- Tweet Generation --------
    with st.spinner("Generating tweets..."):

        tweet_prompt = tweet_generation_prompt(
            brand,
            brand_voice
        )

        tweet_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": tweet_prompt}
            ]
        )

        tweets = tweet_response.choices[0].message.content

    st.subheader("🐦 Generated Tweets")
    st.write(tweets)

    st.success("Tweets generated successfully!")