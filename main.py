from dotenv import load_dotenv
from flask import Flask
from google import genai

app = Flask(__name__)
load_dotenv()
client = genai.Client()


@app.route("/")
def index():
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Give me some kind of variation of 'Hello, World!'. Reply with only that sentence, no extra text.",
    )
    return response.text


# Catch-all just in case
def main():
    print("Run this using the `flask` command")


if __name__ == "__main__":
    main()
