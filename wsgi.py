from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return getinfo()
#    return "Hello World from Trey!"

def getinfo():
  print("Content-type:text/html\r\n\r\n")
  print("<!DOCTYPE html>\n")
  print("<h1>Hello World from function!</h1>\n")
  print("</html>\n")

if __name__ == "__main__":
    application.run()
