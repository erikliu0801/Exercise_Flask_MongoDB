from flask import Flask
app = Flask(__name__)

from controller import getData
@app.route("/")
def web_getData():
    return getData('https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=rdec-key-123-45678-011121314','records')

if __name__ == "__main__":
    app.run()