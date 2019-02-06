fout = open("running-config.cfg",'r')
fout = fout.read()
fout = fout.split("\n")
int_dict = dict()
interface_list = list()
new_list = list()
vlan_check = 0
access_list = []
transit_access_in = []
fw-management_access_in = []

def list_ifname_ip:

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
		if "ip_address" in item:
			if vlan_check == 0:
				interface_list.append("null")
			item=item.split()
        if "net_mask" in item:
			if vlan_check == 0:
				interface_list.append("null")
			item=item.split()    
