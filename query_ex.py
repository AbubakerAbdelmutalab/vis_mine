from requests.auth import HTTPBasicAuth
import requests
import json
from getpass import getpass
import matplotlib.pyplot as plt
from get_connection import get_connection

url = 'https://kibana.emulab.net/elasticsearch/_all/_search'
h = {'content-type':'application/json'}
loaded_query = open("query.json")
json_query = loaded_query.read()
user = "abubaker"
password ="BDf%tJ#VS@6JrAw@9Ktc"
response = requests.post(url, data = json_query,headers=h, auth=get_connection())
if (response.status_code == 401):
	print("HTTP error 401: Client Error, possibly due to incorrect credentials")
	exit()
else:
	response.raise_for_status()

json_response = json.loads(response.text)
hits = json_response['hits']['hits']
file=open('file','a')
for hit in hits:
	log_entry= hit['_source']
	time = log_entry['timestamp']
	message = log_entry['message']
	version = log_entry['@version']
	print(message)
	file.write(message)
file.close()
plt.bar(version, time)
plt.show()
