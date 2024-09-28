from ai21 import AI21Client
# from ai21.chat import ChatMessage

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

def query_library(query, labels=None, path=None):
    response = client.library.answer.create(
        question=query,
        path=path,
        labels=labels,
        model="text-qa",
    )
    print(response)

def get_files():
    # Just return the first 10 files
    response = client.library.files.list(
        offset=0,
        limit=10,
        status="PROCESSED" # Apply 
    )
    print(response)

# Filter the question to documents with the case-sensitive label "hr"
query_library("Hello How are you?")
# print(get_files())



# upload_file("data/course_comments_text/10685.txt")

