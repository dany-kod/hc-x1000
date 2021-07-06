from local_ip import ipLocalSystem as ip
from camera_discovery import cameraDiscovery as cam
from which_check import checkInstalls as wch
from run_node import runNode as runrun

import os
import signal
import atexit


if __name__ == '__main__':
    # test the server..
    print("testing that local Ip can be found.")
    localIp = ip.main()
    print(localIp)


    print("testing camera discover can be found.")
    camera = cam.main()
    print(camera)
    if camera == "Unknown" :
        print("\n\n\nCAMERA WAS NOT FOUND.\nTEST FAILED..\n\n\n")

    print("test we can find nodejs on system.")
    nodejs = wch.main("which node")
    print(nodejs)


    print("test we can run nodejs on system.")
    nodejsCommand = [ nodejs,'keep-image-fresh.js', camera ]
    global trackPid
    trackPid = runrun.main(nodejsCommand)
    print(trackPid)


    print("test we can find ffmpeg on system.")
    findFFmpeg = wch.main("which ffmpeg")
    print(findFFmpeg)


    # now that we have our process created lets declare a function to end it.
    def kill_child():
        if trackPid is None:
            pass
        else:
            print("Process is being killed.")
            os.kill(trackPid, signal.SIGTERM)

    print("test we can kill nodejs after exit.")
    atexit.register(kill_child)
