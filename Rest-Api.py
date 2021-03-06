
import requests
import json
import datetime

mytime = datetime.datetime.now()
print(mytime)

now = datetime.datetime.now()
now.strftime("%I:%M%p on %B %d, %Y")

url = 'http://54.213.153.156:7272/api/v0.1/eaaefbeed081427b8fd74561f396bd41/push'
data_push_statistic = dict(tile='listing', key='id_13', data=json.dumps({"title": "Statistics",
"items": [[" "],["  Mail Recieved on "],["Date : " + now.strftime("%B %d, %Y")],
          ["Time : " + now.strftime("%I:%M%p")],
          [""]]}))

data_push_group_memebrs = dict(tile='listing',
                 key='id_1',
                 data=json.dumps({
                     "title": "Group Memebers",
                     "items": [["\t\tCS 101 GROUP PROJECT"],["Joshua Lilly"],["Behrad Behmardi"],["William Zheng"],["Omnia Elemary"]]}))

data_push_mail_notification = dict(tile='Mail Alert',
                 key='id_2',
                 data=json.dumps({"title": "Mail Notification",
               "description": "number of blockers",
               "big-value": "1 Mail",
               "upper-left-label": "critical:",
               "upper-left-value": "1020",
               "lower-left-label": "major:",
               "lower-left-value": "8609",
               "upper-right-label": "minor:",
               "upper-right-value": "7532",
               "lower-right-label": "all:",
               "lower-right-value": "19 853"}))


data_push_mail_pie_chart = dict(tile='pie_chart', key='id_14',  data=json.dumps({"title": "Mail Analyzation", "pie_data": [["NEW MAil", 1], ["Old Mail", 18], ["Deleted", 50]]}))

data_push_simple_percentage = dict(tile='simple_percentage',
                 key='id_15',
                 data=json.dumps({
                     "title": "CHECKED", "subtitle": "My subtitle", "big_value": "100%",
               "left_value": "50%", "left_label": "Old Mails",
               "right_value": "25%", "right_label": "Unread Mails"}))


r = requests.post(url, data=data_push_mail_notification)
r = requests.post(url, data=data_push_group_memebrs)
r = requests.post(url, data=data_push_statistic)
r = requests.post(url, data=data_push_simple_percentage)
print(r.status_code, r.reason)
print(r.text)
print(r.status_code, r.reason)




