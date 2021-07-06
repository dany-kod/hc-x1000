from local_ip import ipLocalSystem as ip

if __name__ == '__main__':
    # test the server..
    print("testing that local Ip can be found.")
    localIp = ip.main()
    print(localIp)