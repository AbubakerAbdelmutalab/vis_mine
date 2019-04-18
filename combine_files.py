data = []
f1 = []
f2 = []
with open('logs/processed_fix.csv') as f:
	f1 = f.readlines()

with open('logs/processed_geo.csv') as f:
	f2 = f.readlines()


for i,line in enumerate(f1):
	data.append(line.strip('\n').split(',')+f2[i].split(',')[6:])

result = ""
for line in data:
	result += ','.join(line)

with open('logs/processing_geo_fix.csv', 'w') as f:
	f.write(result)