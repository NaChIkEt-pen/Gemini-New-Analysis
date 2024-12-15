import streamlit as st
import google.generativeai as genai
import requests

# Streamlit app
st.title("News Article Analysis with Google Gemini and Fact Check APIs")

# Automatically fetch API keys from secrets
gemini_api_key = st.secrets["GEMINI_API_KEY"]
fact_check_api_key = st.secrets["FACT_CHECK_API_KEY"]

# News article input
news_article = st.text_area("Paste your news article here:", height=200)

# Analysis type selection
analysis_type = st.selectbox(
    "Select the type of analysis:",
    [
        "Summarization",
        "Sentiment Analysis",
        "Key Entities Extraction",
        "Fact Check",
    ],
)

if st.button("Analyze"):
    if not news_article:
        st.error("Please paste a news article.")
    else:
        try:
            # If the user selects Fact Check
            if analysis_type == "Fact Check":
                st.info("Performing Fact Check...")
                
                # Extract claims or key sentences to fact-check (for simplicity, fact-check the entire article)
                fact_check_url = f"https://factchecktools.googleapis.com/v1alpha1/claims:search"
                params = {
                    "query": news_article[:300],  # Limit query size to first 300 chars
                    "key": fact_check_api_key,
                    "pageSize": 5,
                }
                
                response = requests.get(fact_check_url, params=params)
                fact_check_results = response.json()

                # Display Fact Check results
                st.subheader("Fact Check Results:")
                if "claims" in fact_check_results:
                    for claim in fact_check_results["claims"]:
                        claim_text = claim.get("text", "No claim text provided")
                        claimant = claim.get("claimant", "Unknown claimant")
                        st.write(f"**Claim**: {claim_text}")
                        st.write(f"**Claimant**: {claimant}")
                        for review in claim.get("claimReview", []):
                            publisher = review["publisher"]["name"]
                            url = review["url"]
                            title = review["title"]
                            st.write(f"- **Reviewed by**: {publisher}")
                            st.write(f"- **Title**: {title}")
                            st.write(f"- [View Full Review]({url})")
                else:
                    st.write("No fact-check results found for this article.")

            else:
                # For other analysis types (Summarization, Sentiment, Key Entities)
                st.info(f"Performing {analysis_type} using Google Gemini...")
                
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
