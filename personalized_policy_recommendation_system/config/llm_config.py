import os
from groq import Groq

# Initialize Groq client
groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY", "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"))

# Associate the model name with Groq client
clients = {
    'llama3-70b-8192': groq_client
}
