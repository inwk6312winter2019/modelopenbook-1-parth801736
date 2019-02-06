def access_lst(file_name):
	fout = open(file_name)
	lst=[]
	for item in fout:
		item=item.strip()
		for i in item.split():
			if i=='global_access' or i=='fw-management_access_in':	
				lst.append(item)
	return lst

print(access_lst('running-config.cfg'))