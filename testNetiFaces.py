from netifaces import interfaces, ifaddresses, AF_INET
foundIp = 'localhost';
for ifaceName in interfaces():
	for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] ):
		print(i['addr'])
		if i['addr'] != 'No IP addr':
			foundIp = i['addr']

print(foundIp)