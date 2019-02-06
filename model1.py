fout=open("running-config.cfg",'r')
fout=fout.read()
fout=fout.split("\n")
new_list = list()
interface_list = list()
int_dict=dict()
vlan_check = 0