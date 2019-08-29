import requests

import time

file = []
with open('demo_logs/processed.csv') as f: # open a file to process
	for line in f.readlines():
		file.append(line.strip('\n').split(','))


DEMO = True # for time purposes during submission, only query a few IPs
data = []
if DEMO:
	data = file[:20]
else:
	data = file



url = 'https://tools.keycdn.com/geo.json?host={0}'

data[0].append('latitude') # append additional headers
data[0].append('longitude')
data[0].append('city')
data[0].append('country')

unk = 'UNKNOWN'
for line in data[1:]: # request information
	r = requests.get(url.format(line[4]))
	if r.json()['status'] == 'success':
		json = r.json()['data']['geo']
		if json['latitude'] is None:
			line.append(unk)
		else:
			line.append(json['latitude'])
		if json['longitude'] is None:
			line.append(unk)
		else:
			line.append(json['longitude'])
		if json['city'] is None:
			line.append(unk)
		else:
			line.append(json['city'])
		if json['country_name'] is None:
			line.append(unk)
		else:
			line.append(json['country_name'])
	else: # if error, append all unknown
		line.append(unk)
		line.append(unk)
		line.append(unk)
		line.append(unk)
	time.sleep(.4) # wait for approximately 1/3 second

result = ''
for line in data:
	result += ','.join([str(i) for i in line])+'\n'

with open('demo_logs/processed_geo.csv','w') as f: # write new csv
	f.write(result)
