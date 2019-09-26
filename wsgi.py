from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return getinfo()
#    return "Hello World from Trey!"

def getinfo():
  web_con = "<h1>Hello from Flask</h1>\n"
  web_con += "Hello World from function!\n"
  return web_con

if __name__ == "__main__":
    application.run()
