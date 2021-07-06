from netifaces import interfaces, ifaddresses, AF_INET
# I made an external file so to be able to add features when needed.
from server import hcXSERVER

if __name__ == '__main__':
    # run the server..
    hcXSERVER.main()
