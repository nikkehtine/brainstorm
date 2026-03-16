from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Hello from brainstorm!</p>"


# Catch-all just in case
def main():
    print("Run this using the `flask` command")


if __name__ == "__main__":
    main()
