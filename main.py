import streamlit as st
import google.generativeai as genai

# Streamlit app
st.title("News Article Analysis with Google Gemini API")

# Gemini API key input
gemini_api_key = st.text_input("Enter your Gemini API key:", type="password")

# News article input
news_article = st.text_area("Paste your news article here:", height=200)

# Analysis type selection
analysis_type = st.selectbox(
    "Select the type of analysis:",
    ["Summarization", "Sentiment Analysis", "Key Entities Extraction"],
)

if st.button("Analyze"):
    if not gemini_api_key:
        st.error("Please enter your Gemini API key.")
    elif not news_article:
        st.error("Please paste a news article.")
    else:
        try:
            # Configure the Gemini API
            genai.configure(api_key=gemini_api_key)

            # Prepare the prompt based on the analysis type
            if analysis_type == "Summarization":
                prompt = f"Summarize the following news article:\n{news_article}"
            elif analysis_type == "Sentiment Analysis":
                prompt = f"Analyze the sentiment of the following news article (positive, negative, or neutral):\n{news_article}"
            elif analysis_type == "Key Entities Extraction":
                prompt = f"Extract the key entities (people, organizations, locations) mentioned in the following news article:\n{news_article}"

            # Call the Gemini model
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)

            # Display the result
            st.subheader(f"{analysis_type} Result:")
            st.write(response.text)

        except Exception as e:
            st.error(f"An error occurred: {e}")
