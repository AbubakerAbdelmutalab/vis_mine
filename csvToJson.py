import csv
import json

csvfile = open('logs/processed_geo.csv', 'r')
jsonfile = open('web/processed_json.json', 'w')

fieldnames = ("type","timestamp","cluster","node", "sourceip", "user", "latitude", "longitude", "city", "country")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)