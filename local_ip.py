from netifaces import interfaces, ifaddresses, AF_INET

# this will find our local systems ip address for us.
class ipLocalSystem():

	def main():
		foundIp = 'localhost';
		for ifaceName in interfaces():
			for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] ):
				if i['addr'] != 'No IP addr':
					# be partial to 192 addresses
					foundIp = i['addr']
		return foundIp