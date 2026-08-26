# AI Text Assistant

A beginner-friendly Python application that uses an OpenAI language model to transform user-provided text based on a selected task.

## Features

The application supports four text transformation tasks:

- Summarize text
- Rewrite text professionally
- Extract key points
- Generate three questions and answers

## Technologies Used

- Python
- OpenAI API
- Gradio
- python-dotenv

## Project Structure

```text
ai-text-assistant/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
cd ai-text-assistant
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment

On Windows PowerShell:

.venv\Scripts\Activate.ps1

On Windows Command Prompt:

.venv\Scripts\activate.bat
4. Install dependencies
pip install -r requirements.txt
API Key Setup

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here

Do not commit the .env file to GitHub.

The repository includes .env.example as a template.

## How to Run

Start the application with:

python app.py

Gradio will provide a local URL in the terminal. Open that URL in your browser.

Model Used

The application uses the OpenAI model configured in app.py.

## Basic Example
Input

Artificial intelligence helps computers perform tasks that normally require human intelligence. These tasks include understanding language, recognizing images and making decisions.

Selected Task

---> Summarize

Example Output

Artificial intelligence enables computers to perform human-like tasks such as understanding language, recognizing images and making decisions.

## Known Limitations

The application requires an active API connection.
API usage may incur costs depending on the user's OpenAI account and usage limits.
The application has a maximum input length of 5,000 characters.
Generated responses may occasionally contain inaccurate or imperfect information.
The application does not use conversation history or persistent memory.
The application does not use RAG or external knowledge sources.

## Error Handling

The application provides user-friendly messages for common problems such as:

Empty input
Excessively long input
Invalid API credentials
API rate limits
Connection errors
General API errors


