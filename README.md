# News Article Analysis with Google Gemini and Fact Check APIs

This project addresses the challenge of misinformation in digital journalism by leveraging advanced AI technologies from Google. By integrating Google Gemini API and Fact Check Tools API, the system analyzes news articles for biases, validates claims against verified sources, and helps users make informed decisions.

## Project Overview

The project aims to use Google's cutting-edge technologies to evaluate news articles for authenticity and accuracy. It incorporates natural language understanding, sentiment analysis, and fact-checking to provide a robust environment for analyzing and verifying news content.

## Features

1. **News Article Input**:

   - Users can paste the news article text or provide URLs for analysis.
   - Intuitive and interactive interface for a seamless experience.

2. **Analysis Types**:

   - **Summarization**: Generates a concise summary of the article.
   - **Sentiment Analysis**: Identifies the article's sentiment as positive, negative, or neutral.
   - **Key Entities Extraction**: Highlights critical entities like people, organizations, or locations.
   - **Fact Check**: Validates the claims in the article using Google Fact Check API.

3. **Google Gemini API Integration**:

   - Performs natural language processing tasks, including summarization and sentiment analysis.
   - Dynamic prompt generation for diverse NLP functionalities.

4. **Google Fact Check Tools API Integration**:

   - Queries Google's fact-checking database to retrieve verified claims and reviews.
   - Provides detailed claim reviews with publisher information and links to sources.

5. **Error Handling**:

   - Validates user input to ensure a smooth analysis process.
   - Displays meaningful error messages for API-related issues.

6. **User-Friendly Results**:
   - Presents results in a clear, categorized format.
   - Includes links to fact-check reviews for further validation.

## Technology Stack

### Frontend

- **Streamlit**:
  - Creates a user-friendly interface for article submission and analysis options.
  - Dynamic widgets and clean display of analysis results.

### Backend

- **Google Gemini API**:
  - For summarization, sentiment analysis, and key entities extraction.
  - Integrated via the `google.generativeai` Python library.
- **Google Fact Check Tools API**:
  - For validating claims in the article.
  - Integrated using HTTP requests to fetch verified fact-check data.

## Implementation Details

1. **Google Gemini API**:

   - Uses the `gemini-1.5-flash` model for NLP tasks.
   - Tailors analysis based on user-selected options like summarization or sentiment analysis.

2. **Google Fact Check Tools API**:
   - Retrieves verified claims from Google’s database.
   - Processes JSON responses to display claim details, publishers, and review links.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/NaChIkEt-pen/Gemini-New-Analysis.git
   ```

2. Navigate to the project directory and install dependencies:

   ```
   cd Gemini-New-Analysis
   ```

   ```
   pip install -r requirements.txt
   ```

3. Add your API keys to the secrets.toml file:

   ```
   [secrets]
   GEMINI_API_KEY = "your_gemini_api_key"
   FACT_CHECK_API_KEY = "your_fact_check_api_key"
   ```

4. Run the application:

   streamlit run app.py
