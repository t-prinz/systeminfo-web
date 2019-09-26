from flask import Flask
application = Flask(__name__)

########################################

@application.route("/")
def hello():
  web_con = ""

  web_con += pre_write()

  web_con += "hi there\n"

  web_con += post_write()

  return web_con
#  return getinfo(web_con)

########################################

def pre_write():
  local_str = """
  <html>

  <head>

  <style>

#  body {
#      background-color: powderblue;
#  }

  table {
      font-family: arial, sans-serif;
      border-collapse: collapse;
      width: 25%;
  }

  td, th {
      border: 1px solid #dddddd;
      text-align: left;
      padding: 8px;
  }

  tr:nth-child(even) {
      background-color: #dddddd;
  }

  </style>

  </head>

  <body>\n"""

  return local_str

########################################

def post_write():
  local_str = """
  </body>

  </html>\n"""

  return local_str

########################################

def getinfo(local_con):
#  local_con = "<h1>This is a header</h1>\n"
#  local_con += "Hello World from function!\n"

  local_con = """<h1>This is a header</h1>
Hello World from function!\n"""

  return local_con

########################################

if __name__ == "__main__":
    application.run()
