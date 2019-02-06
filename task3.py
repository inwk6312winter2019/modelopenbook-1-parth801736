"""function to create a list of "access-list" for "global_access" and "fw-management_access_in"""

def access_lst(file_name):
	fout = open(file_name)
	lst=[]
	for item in fout:
		item=item.strip()
		for i in item.split():
			if i=='global_access' or i=='fw-management_access_in':	#if the line contains global-access or fw-management it will add that line to list
				lst.append(item)
	return lst

print(access_lst('running-config.cfg'))