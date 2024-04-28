import ollama
import json
import requests
import json
from bs4 import BeautifulSoup
import re


def scrape_text(url):
    response = requests.get(url)

    if response.status_code == 200:

        page_content = response.content
        soup = BeautifulSoup(page_content, "html.parser")
        text = soup.get_text()

        return text
    else:
        return "Failed to scrape the website"
    
def preprocess_text(text):
    text = re.sub(r'http\S+|www.\S+', '', text)
    
    text = re.sub(r'\W', ' ', text)
    return text


def summarize_text(text):
   # Initialize the Ollama client
   client = ollama.Client()
  
   prompt = f"Sumarize the text by incorporating main ideas and essential information, eliminating extraneous language and focusing on critical aspects.Do not include related articles and references Text: {text}"
  
   # Define the request data
   request_data = {
       "model": "mistral",  # Specify the model name as a string
       "prompt": prompt,  # Use the constructed prompt
       "stream": False  # Set to False to receive the full response at once
   }
  
   response = requests.post("http://localhost:11434/api/generate", headers={
       'Content-Type': 'application/json',
   }, data=json.dumps(request_data))
  

   if response.status_code == 200:
       response_data = response.json()
      
       # Extract the summary from the response data
       summary = response_data.get("response", "")
      
       return summary
   else:
       print(f"Error: HTTP {response.status_code} - {response.text}")
       return None

'''
url = "https://research.google/blog/chain-of-table-evolving-tables-in-the-reasoning-chain-for-table-understanding/"
text_to_summarize=preprocess_text(scrape_text(url))

summary_response = summarize_text(text_to_summarize)
print("Summary:")
print(summary_response)
'''
