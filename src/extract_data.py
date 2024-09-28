# Extract data from a structured pdf file

# Each pdf file contains a table with the following sections:
#   Initially it has information about the course, such as the course code, title, and description.

#  Then it has a table with the following sections:
#  It has responses from multiple students to some questions about the course.
#  each question starts with Q: followed by the question and then the responses from the students.
# The responses are indexed by number, followed by the response text.

# The goal is to extract the responses from the students and store them in a structured format.
# The structured format is a dictionary with the following keys:
#   course_code
#   course_title
#   course_description
#   responses

# The responses key will have a list of dictionaries, where each dictionary has the following keys:
#   question
#   responses
# The responses key will have a list of responses from the students.

# The function extract_data_from_pdf takes a file path as input and returns the structured data.
# The function should read the pdf file and extract the data as described above.

# You can use the PyMuPDF library to read the pdf file.
# You can install the library using the following command:
# pip install pymupdf

import pymupdf
import json

def extract_data_from_pdf(file_path):
    # Open the pdf file
    pdf_file = pymupdf.open(file_path)

    # Get the number of pages in the pdf
    num_pages = len(pdf_file)

    # Initialize the structured data dictionary
    structured_data = {
        "course_code": "",
        "course_title": "",
        "course_description": "",
        "responses": []
    }

    # Loop through each page of the pdf
    for page_num in range(num_pages):
        # Get the text content of the page
        page_text = pdf_file[page_num].get_text()

        # Check if the page contains course information
        if "Course ID" in page_text:
            # Extract course code, title, and description
            course_code = page_text.split("Course ID: ")[1].split("\n")[0]
            # course_title = page_text.split("Course Title: ")[1].split("\n")[0]
            # course_description = page_text.split("Course Description: ")[1].split("\n")[0]

            structured_data["crn"] = course_code
            # structured_data["course_title"] = course_title
            # structured_data["course_description"] = course_description

        # Check if the page contains responses
        if "Q:" in page_text:
            # Extract questions and responses
            questions = page_text.split("Q: ")[1:]
            for question in questions:
                question_text = question.split("\n")[0]
                responses = question.split("\n")[1:]
                actual_responses = []
                temp_response = ""
                for response in responses:
                    if response.isdigit():
                        
                        actual_responses.append(temp_response)
                        temp_response = ""
                    else:
                        temp_response += response

                structured_data["responses"].append({
                    "question": question_text,
                    "responses": actual_responses
                })

    # Close the pdf file
    pdf_file.close()
    print(json.dumps(structured_data, indent=4))

    # Use nltk to clean the text
    for response in structured_data["responses"]:
        response["question"] = clean_text(response["question"])
        response["responses"] = [clean_text(r) for r in response["responses"]]
    return structured_data

def clean_text(text):
    # Remove leading and trailing whitespaces
    text = text.strip()
    # Remove special characters
    text = ''.join(e for e in text if e.isalnum() or e.isspace())
    # Convert to lowercase
    text = text.lower()
    return text

file_path = "./data/course_comments/15377.pdf"
extract_data_from_pdf(file_path)