from requests.auth import HTTPBasicAuth
import requests
import json
from getpass import getpass
import matplotlib.pyplot as plt
from get_connection import get_connection

# initial response
url = 'https://kibana.emulab.net/elasticsearch/_all/_search?scroll=1m'
h = {'content-type':'application/json'}
loaded_query = open("query_file.json")
json_query = loaded_query.read()
response = requests.post(url, data = json_query,headers=h, auth=get_connection())
if (response.status_code == 401):
	print("HTTP error 401: Client Error, possibly due to incorrect credentials")
	exit()
else:
	response.raise_for_status()

json_response = json.loads(response.text)
scroll_id = json_response['_scroll_id']
hits = json_response['hits']['hits']
result = "@timestamp\tmessage\n"

for hit in hits:
	log_entry= hit['_source']
	result += log_entry['@timestamp']
	result += "\t"
	result += log_entry['message']
	result += "\n"

with open('logs/10krange_experiment.txt', 'wa') as f:
	f.write(result)

# scroll.... this doesn't work yet
url2 = 'https://kibana.emulab.net/elasticsearch/_all/_search/scroll'
h = {'content-type':'application/json'}

count = 1
while True:
	q = {"scroll":"1m",
	"scroll_id":scroll_id}
	print(scroll_id)
	json_query = json.dumps(q)
	response = requests.post(url2, data = json_query,headers=h, auth=get_connection())
	if (response.status_code == 401):
		print("HTTP error 401: Client Error, possibly due to incorrect credentials")
		exit()
	else:
		response.raise_for_status()
	json_response = json.loads(response.text)

	scroll_id = json_response['_scroll_id']
	hits = json_response['hits']['hits']
	result = "@timestamp\tmessage\n"
	for hit in hits:
		log_entry= hit['_source']
		result += log_entry['@timestamp']
		result += "\t"
		result += log_entry['message']
		result += "\n"
	count ++ 1
	print(count)
	if count == 10:
		with open('logs/100krange_experiemnt.txt', 'wa') as f:
			f.write(result)
		break
	if count == 100:
		with open('logs/1mrange_experiment.txt', 'wa') as f:
			f.write(result)
		break


