from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello. My name is Flask Python. You are on the home page running off of " + __name__

@app.route("/profile/<username>")
def profile(username):
  return "Hello, " + username + "! This is your profile page. The __name__ variable returns " + __name__ + " on this page."

@app.route("/post/<int:post_id>")
def post(post_id):
  return "Post ID is %s" % post_id

if __name__ == "__main__":
  app.run(debug=True, port=8000)