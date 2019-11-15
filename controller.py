import requests
url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=rdec-key-123-45678-011121314'
field = 'records'

def getData(url, field):
    def getJSON(url):
        r = requests.get(url)
        if r.status_code == requests.codes.ok:
            # return r.text #str
            return r.json() #dict
    results_dict = getJSON(url)
    return results_dict[field]

if "__main__" == __name__:
    print(getData(url,'records'))
