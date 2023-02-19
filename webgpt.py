import openai
import requests
from googlesearch import search
from bs4 import BeautifulSoup

# Connect to OpenAI API
openai.api_key = "API_Key_Here"

def webgpt(query):
# Define search query
    num_results = 4

# Perform Google search
    search_results = list(search(query, num_results))

# Loop through search results
    summarized_texts = []
    for url in search_results:
    #Scrape web page content
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
    
        text = ' '.join(text.split()[:100])

    prompt = "what is the main topic of the statement" + text + "when asked the question" + query

    data = {
        "prompt":f"{prompt}",
        "max_tokens":50
    }
    
# Summarize text using GPT-3
    response = openai.Completion.create(engine="text-davinci-003", prompt=data["prompt"], max_tokens=data["max_tokens"])

    return response
