
import csv
import json

csvfile = open('demo_logs/processed_geo.csv', 'r')
jsonfile = open('web/processed_json_demo.json', 'w')

fieldnames = ("type","timestamp","cluster","node", "sourceip", "user", "latitude", "longitude", "city", "country")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write('data = \''+out+'\'')
