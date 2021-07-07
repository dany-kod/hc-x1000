from lib.local_ip import ipLocalSystem as ip
from lib.camera_discovery import cameraDiscovery as cam
from lib.which_check import checkInstalls as wch
from lib.run_node import runNode as runrun
from lib.rouge_images import imageRouge as rouge
from lib.opencv_modify import OpenCvModify
from lib.test import testSystem

from lib.http_api import httpApiServer


import os
import signal
import atexit

import sys
import time

import subprocess as sp
import threading
import requests 

from time import sleep
from xml.etree import ElementTree
from socketserver import ThreadingMixIn

from PIL import Image
import ffmpeg
import numpy
import cv2
import json
from io import BytesIO



class hcXSERVER():
	global hcx1000Address
	global cameraAvaliable
	global WIDTH
	global HEIGHT

	global blank_image
	global opencvFilters
	global regularImage
	global trackPid


	WIDTH = 1280
	HEIGHT = 720

	blank_image = rouge.blank(WIDTH,HEIGHT)
	opencvFilters = False
	regularImage = True
	hcx1000Address = cam.main()
	cameraAvaliable = True
	
	if hcx1000Address == "Unknown" :
		print("\n\n\nCAMERA WAS NOT FOUND.\n\n\n")
		cameraAvaliable = False

# make a condition if camera doesn't exist at all
	if cameraAvaliable : 

		findNode_return = wch.main("which node")
		if len(findNode_return) == 0 :
			print("Node is not installed.")
		nodejsCommand = [ findNode_return,'keep-image-fresh.js', hcx1000Address ]
		# Here you can get the PID
		trackPid = runrun.main(nodejsCommand)
		print(trackPid)

		FFMPEG_BIN = wch.main("which ffmpeg")
		if len(FFMPEG_BIN) == 0 :
			print("ffmpeg is not installed.")

		command = [ FFMPEG_BIN,
					'-hide_banner',
					'-loglevel', 'panic', 
					'-f', 'mjpeg',
					#'-r','30',
					'-i', 'udp://'+str(hcx1000Address)+':9100?overrun_nonfatal=1',             # fifo is the named pipe 
					'-pix_fmt', 'bgr24',      # opencv requires bgr24 pixel format.
					'-vcodec', 'rawvideo',
					'-s', str(WIDTH)+'x'+str(HEIGHT), # size of one frame
					'-an','-sn',              # we want to disable audio processing (there is no audio)
					'-f', 'image2pipe', '-']
		global pipe
		pipe = runrun.rawCommand(command)

	def getTracks():
		return trackPid
	# prepare a default image
	
	def getLocalIp():
		return ip.main();

	def main():
		global locationServer
		locationServer = hcXSERVER.getLocalIp()
		PORTNUMBER = 7099
		try:
			server = httpApiServer.ThreadedHTTPServer((locationServer, PORTNUMBER), httpApiServer.cameraHTTPSERVER)
			print( "camera api server started, visit http://"+locationServer+":"+str(PORTNUMBER)+"/")
			server.serve_forever()
		except KeyboardInterrupt:
			server.socket.close()

	def kill_child():
		if trackPid is None:
			pass
		else:
			os.kill(trackPid, signal.SIGTERM)

	atexit.register(kill_child)