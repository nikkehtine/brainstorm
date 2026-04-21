import time

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173"]}})

system_prompt = (
    "You are a programming/data science project idea generator. You only respond to requests about generating ideas for projects "
    "related to programming, software engineering, web development, and data science. Ignore all unrelated requests."
    "\n\n"
    "For the project ideas, try to come up with ideas that are enjoyable to both work on and then use. Avoid boring, generic, "
    "cookie-cutter projects, like to-do list apps, portfolio websites, or simple CRUD apps. "
    "Projects should be achievable through self-directed learning using official documentation and common learning resources. "
    "Prefer solutions that use as few external libraries or frameworks as possible, and only suggest using abstraction "
    "if it's essential for the project's core idea."
    "\n\n"
    "Format your response in Markdown and use second-level headings for each project name, as follows:\n"
    "## Project Name\n"
    "Brief description of the project (2-3 sentences).\n"
    "### Features\n"
    "A bullet-point list of basic features to implement first.\n"
    "### Extensions\n"
    "A bullet-point list of additional features to implement later for extra challenge.\n"
    "### Look Into\n"
    "A bullet-point list of libraries or concepts to learn more about. Only include what is directly relevant and try to avoid "
    "abstractions for features the user could implement themselves. Avoid outdated libraries or concepts.\n"
    "Be concise - do not add preamble or filler text. Do not ask any follow up questions."
)


@app.route("/doot")
def index():
    contents = generate_response(
        "Generate a simple tagline for a programming project idea generator. Reply in a single sentence."
    )
    if not contents:
        return jsonify({"error": "Error generating response"}), 500
    return contents


def generate_response(prompt: str) -> str | None:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        # config=types.GenerateContentConfig(system_instruction=system_prompt),
        contents=prompt,
    )
    return response.text


@app.route("/time")
def get_current_time():
    return {"time": time.time()}


# Catch-all just in case
if __name__ == "__main__":
    print("Run this using the `flask` command")
