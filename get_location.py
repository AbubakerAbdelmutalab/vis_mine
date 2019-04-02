import requests
import time

data = []
with open('logs/processed_test.csv') as f:
	for line in f.readlines():
		data.append(line.strip('\n').split(','))

url = 'https://tools.keycdn.com/geo.json?host={0}'

data[0].append('latitude')
data[0].append('longitude')
data[0].append('city')
data[0].append('country')

for line in data[1:]:
	r = requests.get(url.format(line[4]))
	if r.json()['status'] == 'success':
		json = r.json()['data']['geo']
		line.append(json['latitude'])
		line.append(json['longitude'])
		line.append(json['city'])
		line.append(json['country_name'])
	else:
		line.append('UNKNOWN')
		line.append('UNKNOWN')
		line.append('UNKNOWN')
		line.append('UNKNOWN')
	time.sleep(.4)

result = ''
for line in data:
	result += ','.join([str(i) for i in line])+'\n'

with open('logs/processed_geo.csv','w') as f:
	f.write(result)
