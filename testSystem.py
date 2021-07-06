from local_ip import ipLocalSystem as ip
from camera_discovery import cameraDiscovery as cam

if __name__ == '__main__':
    # test the server..
    print("testing that local Ip can be found.")
    localIp = ip.main()
    print(localIp)


    print("testing camera discover can be found.")
    camera = cam.main()
    print(camera)