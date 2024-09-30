from langchain_nvidia_ai_endpoints import ChatNVIDIA
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Configuration of the Ollama API client using the environment variable
client = ChatNVIDIA(
    model="meta/llama-3.2-3b-instruct",
    api_key=os.getenv("API_KEY"),  # Retrieving the API key from the environment variable
    temperature=0.2,
    top_p=0.7,
    max_tokens=1024,
)

def get_code_suggestions(problem_input, request_input):
    """
    Retrieve code suggestions from the Ollama API based on the provided problem and request.

    This function takes in a programming problem and a desired outcome from the user, 
    constructs a prompt, and sends it to the Ollama model for suggestions. 
    The response is streamed and concatenated into a single output string.

    Args:
        problem_input (str): A description of the programming problem the user is facing.
        request_input (str): A description of what the user wants to achieve or improve in their code.

    Returns:
        str: A concatenated string containing the suggestions provided by the Ollama model. 
             If no suggestions are returned, an empty string is returned.
    """
    response = client.stream([{"role": "user", "content": f"Problema: {problem_input}\nDesejo: {request_input}"}])
    
    output_text = ""  # Initialize the output text variable
    for chunk in response:
        output_text += chunk.content  # Concatenate the response
    
    return output_text
