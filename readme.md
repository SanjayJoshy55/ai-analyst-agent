# AI News Analyst Agent  
**Assignment 2 Submission**

## Project Overview  
This project is an automated AI agent that tracks and analyzes news about AI startups. It fulfills all the requirements of Assignment 2 using Python, NewsAPI, and Google Gemini to implement a complete data pipeline.

The agent performs the following tasks automatically:
1.Fetches real-time news articles using NewsAPI.
2.Cleans the data by removing duplicates and filtering out low-quality marketing articles.
3.Uses the Gemini 2.5 Flash LLM to extract sentiment, funding details, and summaries from each article.
4.Stores the processed results in a structured CSV file, which can be used to build dashboards.

## System Architecture  
The system includes multiple stages such as data fetching, deduplication, filtering, AI-based analysis, and storage.  
Refer to **diagram.png** for the complete logic flow of the pipeline, including the deduplication and filtering components that help optimize API usage.

---

## How to Run Locally

### 1. Install Dependencies  
Open your terminal in the project directory and run:
```bash
pip install -r requirements.txt
2. Configure API Keys
Open the config.py file and replace the placeholder values with your own API keys:

NEWS_API_KEY: Register at https://newsapi.org

GEMINI_API_KEY: Get your key from https://aistudio.google.com

These keys are required for fetching news articles and using the Gemini model for analysis.

3. Run the Agent
Start the pipeline using:

bash
Copy code
python main.py

Output and Dashboard
After execution, a file named ai_startup_data.csv will be generated in the samples/ folder.

This file includes:

Cleaned article data

Summary and sentiment analysis

Funding information


Files_Included
File_Name	                     Description
main.py	                         Main controller that runs the entire process
news_client.py	                 Handles API calls to fetch news articles
llm_client.py	                 Sends articles to Gemini for analysis
deduplication.py	             Removes duplicate articles
hype_filter.py	                 Filters out low-quality or promotional articles
diagram.png	                     Flowchart of the system architecture
samples/ai_startup_data.csv	     Final output file 
dashboard.pbix                   sample Dashboard created using PowerBI

youtube link https://youtu.be/4IkDyThwUBI
