import platform

from flask import Flask
application = Flask(__name__)

########################################

@application.route("/")
def hello():
  web_con = ""

  web_con += pre_write()

  web_con += get_info()

  web_con += post_write()

  return web_con

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

def get_info():
  local_str = ""

  # Start a new table to show the basic system information

  local_str += """
  <h2>System Information</h2>

  <table>
    <tr>
      <th>Parameter</th>
      <th>Value</th>
    </tr>\n"""

#  # Populate the table

#  print("  <tr>\n")
#  print("    <td>Hostname</td>\n")
#  print("    <td>{}</td>\n".format( platform.node() ))
#  print("  </tr>\n")

#  print("  <tr>\n")
#  print("    <td>System</td>\n")
#  print("    <td>{}</td>\n".format( platform.system() ))
#  print("  </tr>\n")

#  print("  <tr>\n")
#  print("    <td>Release</td>\n")
#  print("    <td>{}</td>\n".format( platform.release() ))
#  print("  </tr>\n")

  # Finish the table

  local_str += "  </table>\n"

  return local_str

########################################

if __name__ == "__main__":
    application.run()
