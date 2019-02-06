"""Write a Python function called "list_ifname_ip" to scan 
the configuration and return a dictionary that contains 
the "nameif" as the key and "IPaddress,NetMask" tuple as the value."""

fout = open("running-config.cfg",'r')
fout = fout.read()
fout = fout.split("\n")

int_dict = dict()
interface_list = list()
new_list = list()
vlan_check = 0

def list_of_tuple():

	for item in fout:
	
		if "interface" in item:
			item= item.split()
			interface_list.append(item[1])
	
		if "nameif" in item:
			item=item.split()
			if "no" in item[0]:
				interface_list.append("null")
				new_list.append(tuple(interface_list))
				del interface_list[:]
			else:
				interface_list.append(item[1])
				new_list.append(tuple(interface_list))
				del interface_list[:]
	return new_list

def list_ifname_ip():
	
	global vlan_check
	
	for item in fout:
	
		if "interface" in item:
			item=item.split()
			interface_list.append(item[1])
	
		if "nameif" in item:
			item=item.split()
			if "no" in item[0]:
				interface_list.append("null")
			else:
				interface_list.append(item[1])
	
		if "vlan" in item:
			item=item.split()
			interface_list.append(item[1])
			vlan_check = 1
	
		if "ip address" in item:
			if vlan_check == 0:
				interface_list.append("null")
			item=item.split()
			if "no" in item[0]:
				interface_list.append("null")
				interface_list.append("null")
				int_dict[interface_list[0]]=interface_list[1:]
				del interface_list[:]
				vlan_check = 0
			else:
				interface_list.append(item[2])
				interface_list.append(item[3])
				int_dict[interface_list[0]]=interface_list[1:]
				del interface_list[:]
				vlan_check = 0
	return int_dict

print(list_ifname_ip())