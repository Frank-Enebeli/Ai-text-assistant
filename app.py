import os

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
from openai import APIConnectionError, APIError, AuthenticationError, RateLimitError

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY was not found in the .env file.")

client = OpenAI(api_key=api_key)

PROMPTS = {
    "summarize": "Summarize the following text clearly and concisely:",
    "professional": "Rewrite the following text in a professional tone:",
    "key_points": "Extract the main points from the following text:",
    "quiz": "Create three questions and answers based on the following text:",
}

MAX_LENGTH = 5000

def transform_text(text, task):
    if not text or not text.strip():
        return "Please enter some text."

    text = text.strip()

    if len(text) > MAX_LENGTH:
        return (
            f"Your text is too long. "
            f"Please keep it under {MAX_LENGTH} characters."
        )

    if task not in PROMPTS:
        return "Please select a valid task."
        



    prompt = f"""{PROMPTS[task]}

Text to transform:
{text}
"""
    try:
        response = client.responses.create(
        model="gpt-5-nano",
        input=prompt
    )

        return response.output_text

    except AuthenticationError:
        return "Authentication failed. Please check the API key."

    except RateLimitError:
        return "The API limit has been reached. Please try again later."

    except APIConnectionError:
        return "Unable to connect to the AI service. Please check your internet connection."

    except APIError:
        return "The AI service returned an error. Please try again."

    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Something unexpected went wrong. Please try again."

interface = gr.Interface(
    fn=transform_text,
    inputs=[
        gr.Textbox(
            label="Enter your text",
            placeholder="Paste the text you want to transform here...",
            lines=10,
            max_length=MAX_LENGTH
        ),
        gr.Dropdown(
            choices=[
                ("Summarize", "summarize"),
                ("Rewrite Professionally", "professional"),
                ("Extract Key Points", "key_points"),
                ("Generate Questions & Answers", "quiz"),
            ],
            label="Select a task",
            value="summarize"
        ),
    ],
    outputs=gr.Textbox(
        label="Result",
        lines=10
    ),
    title="AI Text Assistant",
    description="Paste your text, choose a task, and let AI transform it."
)

if __name__ == "__main__":
    interface.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))