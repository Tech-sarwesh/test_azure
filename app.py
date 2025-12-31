from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Friend!  This is Azure CI-CD Demo App."

if __name__ == "__main__":
    app.run()
