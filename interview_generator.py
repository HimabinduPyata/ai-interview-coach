import os
from openai import OpenAI

# Load API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_questions(job_title, job_description):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an experienced software engineering interviewer. "
                    "Generate interview preparation material based on the job description."
                )
            },
            {
                "role": "user",
                "content": f"""
Job Title:
{job_title}

Job Description:
{job_description}

Please generate:

1. Five technical interview questions.
2. Three behavioral interview questions.
3. Two system design topics.
4. Five important skills or concepts to review.

Format the response clearly with section headings.
"""
            }
        ]
    )

    return response.choices[0].message.content