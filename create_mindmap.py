import ollama

def generate_markmap(text):
   # Initialize the Ollama client
   client = ollama.Client()
  
   # Define the prompt for generating a mindmap from the text
   prompt = (
       "Please convert the given article into a markdown file suitable for creating a visual mindmap. "
       "Keep sentences short and focused, and emphasize key points with headings and bullet points. "
       "Text: " + text
   )
  
   # Define the request data
   request_data = {
       "model": "mistral",  # Specify the model name as a string
       "prompt": prompt,  # Use the constructed prompt
       "stream": False  # Set to False to receive the full response at once
   }
  
   # Send the request and get the response
   response = client.generate(
       model=request_data["model"],
       prompt=request_data["prompt"],
       stream=request_data["stream"]
   )
  
   # Check the response for the output
   if isinstance(response, dict):
       markdown_output = response.get("response", "")
       # Process the markdown_output if necessary
       # For example, wrap long lines if needed
       return markdown_output
   else:
       print("Unexpected response format")
       return None


