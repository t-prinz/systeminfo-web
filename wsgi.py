from flask import Flask
application = Flask(__name__)

########################################

@application.route("/")
def hello():
  web_con = ""
  return getinfo(web_con)

########################################

def getinfo(local_con):
  local_con = "<h1>This is a header</h1>\n"
  local_con += "Hello World from function!\n"

#  local_con = """<h1>This is a header</h1>\n
#Hello World from function!\n"""

  return local_con

########################################

if __name__ == "__main__":
    application.run()
