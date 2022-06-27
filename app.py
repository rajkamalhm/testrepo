from flask import Flask
app = Flask(__name__)

# Adding new feature
@app.route("/")
def hello():
    return "Hello World!"
 
if __name__ == "__main__":
    app.run()
