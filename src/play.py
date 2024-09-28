from ai21 import AI21Client
from ai21.chat import ChatMessage

# Load api key from .env file
import os
from dotenv import load_dotenv
load_dotenv()

AI21_API_KEY = os.getenv("AI21_API_KEY")

client = AI21Client(
    api_key=AI21_API_KEY
)

def upload_file(file_path):
    crn = file_path.split("/")[-1].split(".")[0]
    labels = [f"Course reviews for course with CRN : {crn}"]
    
    response = client.library.files.create(file_path=file_path, labels=labels)

    print(response)
    return response



