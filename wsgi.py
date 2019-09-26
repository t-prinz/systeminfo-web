from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return getinfo()
#    return "Hello World from Trey!"

def getinfo():
  print("<!doctype html>")
  print("<title>Hello from Flask</title>")

if __name__ == "__main__":
    application.run()
