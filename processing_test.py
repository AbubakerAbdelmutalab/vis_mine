import re


data = []
with open('logs/10krange.txt') as f:
	for line in f.readlines()[1:]:
		data.append(line.split('\t'))


# TYPES

INVALID_USER = 'INVALID_USER'
FAILED_PASSWORD = 'FAILED_PASSWORD'
DISCONNECT = 'DISCONNECT'
DISCONNECT_FROM_USER = 'DISCONNECT_INVALID_USER'
ACCEPT_PUBLIC_KEY = 'ACCEPT_PUBLIC_KEY'
DISCONNECT_PREAUTH = 'DISCONNECT_PREAUTH'
REVERSE_MAPPING = 'REVERSE_MAPPING'
DISCONNECT_INVALID_USER = 'DISCONNECT_INVALID_USER'
TOO_MANY_PASSWORD_ATTEMPTS = 'TOO_MANY_PASSWORD_ATTEMPTS'
UNABLE_TO_NEGOTIATE = 'UNABLE_TO_NEGOTIATE'
NEW_SESSION = 'NEW_SESSION'
REMOVE_SESSION = 'REMOVE_SESSION'
NO_IDENTIFICATION = 'NO_IDENTIFICATION'

ip_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
disc_inv_pattern = r'disconnected\sfrom\sinvalid\suser\s(.+)'
inv_pass = r'failed\spassword\sfor\s(.+)'
inv_user = r'(invalid|illegal)\suser\s(.+)\sfrom'
inv_user_2 = r'invalid\suser\s(.+)\s\['
accept = r'accepted\spublickey'
too_many = r'too\smany\sauthentication\sfailures\sfor\s(.+)'
maximum = r'maximum\sauthentication\sattempts\sexceeded\sfor\s(.+)'
unable = r'unable\sto\snegotiate'
reverse = r'reverse\smapping\schecking\sgetaddrinfo\sfor\s(.+)\s\['
disc_preauth = r'(disconnect|closed).+\[preauth\]'
disc_by_user = r'disconnected\sby\suser'
disconnect_base = r'disconnect'
new_sess = r'new\ssession.+user\s(.+)\.'
remove_sess = r'removed\ssession'
no_id = r'did\snot\sreceive\sidentification\sstring'


processed = []
for line in data:
	timestamp = line[0]
	clust = None
	node = None
	ip = None
	type = None
	user = None

	msg = line[1].lower()
	found = re.search(ip_pattern,msg)
	if found: # only use messages with a source ip
		ip = found.group(0)
	else:
		ip = "UNKNOWN"
	msg_split = line[1].split()
	clust = msg_split[3]
	node = msg_split[4]
	if 'ssh' in node:
		node = 'UNKNOWN'

	found = re.search(disc_inv_pattern,msg)
	if found and type==None:
		user = "other"#found.group(1)
		type = DISCONNECT_INVALID_USER

	found = re.search(inv_pass,msg)
	if found and type==None:
		user = found.group(1)
		if user != 'root':
			user = 'other'
		type = FAILED_PASSWORD

	found = re.search(inv_user,msg)
	if found and type==None:
		user = 'other'
		type = INVALID_USER

	found = re.search(inv_user_2,msg)
	if found and type==None:
		user = 'other'
		type = INVALID_USER

	found = re.search(accept,msg)
	if found and type==None:
		type = ACCEPT_PUBLIC_KEY

	found = re.search(accept,msg)
	if found and type==None:
		type = ACCEPT_PUBLIC_KEY

	found = re.search(too_many,msg)
	if found and type==None:
		user = found.group(1)
		if user != 'root':
			user = 'other'
		type = TOO_MANY_PASSWORD_ATTEMPTS

	found = re.search(maximum,msg)
	if found and type==None:
		user = found.group(1)
		if user != 'root':
			user = 'other'
		type = TOO_MANY_PASSWORD_ATTEMPTS

	found = re.search(unable,msg)
	if found and type==None:
		type = UNABLE_TO_NEGOTIATE

	found = re.search(reverse,msg)
	if found and type==None:
		user = found.group(1)
		type = REVERSE_MAPPING

	found = re.search(disc_preauth,msg)
	if found and type==None:
		type = UNABLE_TO_NEGOTIATE

	found = re.search(disc_preauth,msg)
	if found and type==None:
		type = DISCONNECT_PREAUTH

	found = re.search(disc_by_user,msg)
	if found and type==None:
		type = DISCONNECT_FROM_USER

	found = re.search(disconnect_base,msg)
	if found and type==None:
		type = DISCONNECT

	found = re.search(new_sess,msg)
	if found and type==None:
		user = 'other'
		type = NEW_SESSION

	found = re.search(remove_sess,msg)
	if found and type==None:
		type = REMOVE_SESSION

	found = re.search(no_id,msg)
	if found and type==None:
		type = NO_IDENTIFICATION

	if type==None:
		print(msg)
		continue
	if user==None:
		user = 'UNKNOWN'

	processed.append((type,timestamp,clust,node,ip,user))

#print(processed[:500])
result = 'type,timestamp,cluster,node,sourceip,user\n'
for line in processed:
	result += ','.join([str(i) for i in line])+'\n'

with open('logs/processed_test.csv','w') as f:
	f.write(result)

