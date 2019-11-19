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


"""
models imports app, but app does not import models so we haven't created
any loops.
"""
# import datetime

# from flask_peewee.auth import BaseUser  # provides password helpers..
# from peewee import *

# from app import db


# class User(db.Model, BaseUser):
#     username = CharField()
#     password = CharField()
#     email = CharField()
#     join_date = DateTimeField(default=datetime.datetime.now)
#     active = BooleanField(default=True)
#     admin = BooleanField(default=False)

#     def __unicode__(self):
#         return self.username