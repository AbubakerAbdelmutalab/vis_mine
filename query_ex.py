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
response = requests.post(url, data = json_query,headers=h, auth=get_connection())
if (response.status_code == 401):
	print("HTTP error 401: Client Error, possibly due to incorrect credentials")
	exit()
else:
	response.raise_for_status()

json_response = json.loads(response.text)
hits = json_response['hits']['hits']
file=open('file','a')
time = []
version = []
filter_version = []
category = {"REQUEST": 0, "REPLY(0)": 0, "REPLY(1)": 0, "SEND": 0}
print(len(hits))
for hit in hits:
	log_entry= hit['_source']
	time.append(log_entry['@timestamp'])
	message = log_entry['message']
	if "REQUEST" in message:
		category["REQUEST"] += 1
	elif "REPLY(0)" in message:
		category["REPLY(0)"] += 1
	elif "REPLY(1)" in message:
		category["REPLY(1)"] += 1
	elif "SEND" in message:
		category["SEND"] += 1
	version.append(log_entry['@version'])
	filter_version.append(log_entry['logstash_filter_version'])
	#print(message)
	#file.write(message)
#file.close()
print category
plt.bar(list(category.keys()), list(category.values()))
#plt.hist(version)
#plt.show()
plt.savefig("graphs/category_from_bootinfo.png")

