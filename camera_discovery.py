from netdisco.discovery import NetworkDiscovery
# this will find our local systems ip address for us.
class cameraDiscovery():
    def main():
        hcx1000Address = "Unknown";
        netdis = NetworkDiscovery()
        netdis.scan()
        for dev in netdis.discover():
            for i in netdis.get_info(dev):
                if i['name'].find("X1000") != -1 :
                    hcx1000Address = i['host']
        netdis.stop()
        return hcx1000Address