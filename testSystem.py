from local_ip import ipLocalSystem as ip
from camera_discovery import cameraDiscovery as cam
from which_check import checkInstalls as wch

if __name__ == '__main__':
    # test the server..
    print("testing that local Ip can be found.")
    localIp = ip.main()
    print(localIp)


    print("testing camera discover can be found.")
    camera = cam.main()
    print(camera)


    print("test we can find nodejs on system.")
    nodejs = wch.main("which node")
    print(nodejs)