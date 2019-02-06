def replace_ip(file_name):
	file=open(file_name)

	lst=[]
	lst2=[]	#contains all ip address
	lst3=[]	#contains list of elements in ip address
	lst4=[]	#list of updated ip address  
	
    for item in file:
	
    	item=item.strip()
	
  for word in item.split():
			lst.append(word)
	
    for i in range(len(lst)):
		if lst[i-1]!='no' and lst[i]=='ip' and lst[i+1]=='address':
			lst2.append(lst[i+2])	#add all ip in address lst2
	
    for i in lst2:
		lst3.append(i.split('.'))	#list of elements address in ip
	
    for i in lst3:		#replace '172' or '192' with '10'
		i[0]='10'	#add update ip
		lst4.append('.'.join(i))	#add upated ip in address list
	return lst4

print(replace_ip('running-config.cfg'))