from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from flask import Flask

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'


app = Flask(__name__)

def sheet_html():
    html = ""
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '15x7du76qNipcTxDD9_bLCZ9evwteqzTechFX7j_Ti8w'
    RANGE_NAME = 'A2:D102'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        return "No data found."
    else:
        html = "<table>"
        html += "<th>id</th><th>Name</th><th>Email</th><th>Fake Credit Card</th>"
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            html += "<tr>"
            html += "<td>" + row[0] + "</td>"
            html += "<td>" + row[1] + "</td>"
            html += "<td>" + row[2] + "</td>"
            html += "<td>" + row[3] + "</td>"
            html += "</tr>"
            
        html += "</table>"
        return html;

def header():
  html = "<h1>Python Website Proof of Concept</h1>"
  html += "<ol>"
  html += "<li><a href='/sheets'>Connecting to a Google Sheet with Python</a></li>"
  html += "<li><a href='/profile/username'>Demonstrating a get parameter at /profile/username</a></li>"
  html += "<li><a href='/post/1'>Demonstrating an integer parameter with /post/1</a></li>"
  html += "</ol>"
  return html
      
@app.route("/")
def index():
  
  return header()

@app.route("/sheets")
def sheets():
  html = header()
  html += sheet_html()
  return html

@app.route("/profile/<username>")
def profile(username):
  html = header()
  html += "Hello, " + username + "! This is your profile page. The __name__ variable returns " + __name__ + " on this page."
  return html

@app.route("/post/<int:post_id>")
def post(post_id):
  html = header()
  html += "Post ID is %s" % post_id
  return html

if __name__ == "__main__":
  app.run(debug=True, port=8000)