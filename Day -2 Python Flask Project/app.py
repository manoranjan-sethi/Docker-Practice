from flask import Flask

app = Flask(__name__)

@app.route("/info")
def wish():
    return "<h1>Good Morining from Docker!</h1>"

@app.route("/login")
def login():
    return "<h1>Login Page of Docker!</h1>"

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
