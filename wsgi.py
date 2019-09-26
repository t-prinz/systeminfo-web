from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return getinfo()
#    return "Hello World from Trey!"

def getinfo():
  print("Hello World from function!")

if __name__ == "__main__":
    application.run()
