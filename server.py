import sys
import time
import os
import signal
import atexit

import subprocess as sp
import threading
import requests 

from time import sleep
from xml.etree import ElementTree
from netifaces import interfaces, ifaddresses, AF_INET
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from opencv_modify import OpenCvModify

from PIL import Image
import ffmpeg
import numpy
from netdisco.discovery import NetworkDiscovery
import cv2
import json
from io import BytesIO



class hcXSERVER():
	global hcx1000Address
	hcx1000Address = None
	netdis = NetworkDiscovery()
	netdis.scan()
	for dev in netdis.discover():
		for i in netdis.get_info(dev):
			if i['name'].find("X1000") != -1 :
				hcx1000Address = i['host']
	netdis.stop()
	global WIDTH
	WIDTH = 1280
	global HEIGHT
	HEIGHT = 720

	global cameraAvaliable
	cameraAvaliable = True
	# make a condition if camera doesn't exist at all
	if hcx1000Address == None :
		print("\n\n\nCAMERA WAS NOT FOUND.\n\n\n")
		cameraAvaliable = False

	if cameraAvaliable : 
		findNode = sp.Popen("which node", shell=True, stdout=sp.PIPE)
		findNode_return = findNode.stdout.read().strip()
		if len(findNode_return) == 0 :
			print("Node is not installed.")

		nodejsCommand = [ findNode_return,'keep-image-fresh.js', hcx1000Address ]
		nodejs = sp.Popen(nodejsCommand, stdin=None, stdout=None, stderr=None, close_fds=True)
		# Here you can get the PID
		global child_pid
		child_pid = nodejs.pid
		print(child_pid)

		findFFmpeg = sp.Popen("which ffmpeg", shell=True, stdout=sp.PIPE)
		findFFmpeg_return = findFFmpeg.stdout.read().strip()
		if len(findFFmpeg_return) == 0 :
			print("ffmpeg is not installed.")
		# location of ffmpeg
		FFMPEG_BIN = findFFmpeg_return
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
		pipe = sp.Popen(command, stdout = sp.PIPE)

	global regularImage
	regularImage = True
	# prepare a default image
	global blank_image
	blank_image = numpy.zeros((HEIGHT,WIDTH,3), numpy.uint8)

	class cameraHTTPSERVER(BaseHTTPRequestHandler):

		def do_GET(self):
			if len(self.path) == 1:
				# this is root.. lets give them index page
				root = os.path.dirname(os.path.abspath(__file__))
				filename = root +'/index.html'
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				with open(filename, 'rb') as fh:
					html = fh.read()
					self.wfile.write(html)
				return
			if self.path.endswith('hx.mjpg'):
				self.send_response(200)
				self.send_header('Content-type','multipart/x-mixed-replace; boundary=--jpgboundary')
				self.end_headers()
				while True:
					try:
						if cameraAvaliable :
							raw_image = pipe.stdout.read(WIDTH*HEIGHT*3)
						else :
							raw_image = 0

	                    # transform the byte read into a numpy array
						if len(raw_image) != 0 :
							image =  numpy.fromstring(raw_image, dtype='uint8')

							image = image.reshape((HEIGHT,WIDTH,3))          # Notice how height is specified first and then width
							#image = OpenCvModify.modBrightness(image, 50)
							topLeft = (0, 640)
							bottomRight = (WIDTH, HEIGHT)
							xl, yl = topLeft[0], topLeft[1]
							wl, hl = bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]
							# Grab ROI with Numpy slicing and blur
							ROI = image[yl:yl+hl, xl:xl+wl]
							blur = cv2.GaussianBlur(ROI, (1,1), 0) 
							image[yl:yl+hl, xl:xl+wl] = blur
							if regularImage :
								imgRGB=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
							else :
								imgRGB=cv2.cvtColor(blank_image,cv2.COLOR_BGR2RGB)
						else :
							imgRGB=cv2.cvtColor(blank_image,cv2.COLOR_BGR2RGB)
						jpg = Image.fromarray(imgRGB)
						tmpFile = BytesIO()
						jpg.save(tmpFile,'JPEG')
						self.wfile.write("--jpgboundary".encode())
						self.send_header('Content-type','image/jpeg')
						self.send_header('Content-length',str(tmpFile.getbuffer().nbytes))
						self.end_headers()
						jpg.save(self.wfile,'JPEG')
						time.sleep(0.05)
					except KeyboardInterrupt:
						break
				return

			if self.path.endswith('api/zoomin'):
				self.send_response(200)
				self.send_header('Content-type','application/json')
				self.end_headers()
				r = requests.get('http://'+str(hcx1000Address)+'/cam.cgi?mode=camcmd&value=tele-normal')
				your_json = '["success"]'
				parsed = json.loads(your_json)
				self.wfile.write((json.dumps(parsed, indent=4, sort_keys=True)).encode())
				return
			if self.path.endswith('api/zoomout'):
				self.send_response(200)
				self.send_header('Content-type','application/json')
				self.end_headers()
				r = requests.get('http://'+str(hcx1000Address)+'/cam.cgi?mode=camcmd&value=wide-normal')
				your_json = '["success"]'
				parsed = json.loads(your_json)
				self.wfile.write((json.dumps(parsed, indent=4, sort_keys=True)).encode())
				return
			if self.path.endswith('api/zoomstop'):
				self.send_response(200)
				self.send_header('Content-type','application/json')
				self.end_headers()
				r = requests.get('http://'+str(hcx1000Address)+'/cam.cgi?mode=camcmd&value=zoomstop')
				your_json = '["success"]'
				parsed = json.loads(your_json)
				self.wfile.write((json.dumps(parsed, indent=4, sort_keys=True)).encode())
				return
			if self.path.endswith('api/autofc'):
				self.send_response(200)
				self.send_header('Content-type','application/json')
				self.end_headers()
				r = requests.get('http://'+str(hcx1000Address)+'/cam.cgi?mode=camcmd&value=pushaf')
				your_json = '["success"]'
				parsed = json.loads(your_json)
				self.wfile.write((json.dumps(parsed, indent=4, sort_keys=True)).encode())
				return
			if self.path.endswith('api/outfast'):
				self.send_response(200)
				self.send_header('Content-type','application/json')
				self.end_headers()
				r = requests.get('http://'+str(hcx1000Address)+'/cam.cgi?mode=camcmd&value=wide-fast')
				your_json = '["success"]'
				parsed = json.loads(your_json)
				self.wfile.write((json.dumps(parsed, indent=4, sort_keys=True)).encode())
				return
			if self.path.endswith('api/infast'):
				self.send_response(200)
				self.send_header('Content-type','application/json')
				self.end_headers()
				r = requests.get('http://'+str(hcx1000Address)+'/cam.cgi?mode=camcmd&value=tele-fast')
				your_json = '["success"]'
				parsed = json.loads(your_json)
				self.wfile.write((json.dumps(parsed, indent=4, sort_keys=True)).encode())
				return

	class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
		"""Handle requests in a separate thread."""

	def getLocalIp():
		foundIp = 'localhost';
		for ifaceName in interfaces():
			for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] ):
				if i['addr'] != 'No IP addr':
					foundIp = i['addr']
		return foundIp

	def main():
		global locationServer
		locationServer = hcXSERVER.getLocalIp()
		PORTNUMBER = 7099
		try:
			server = hcXSERVER.ThreadedHTTPServer((locationServer, PORTNUMBER), hcXSERVER.cameraHTTPSERVER)
			print( "camera api server started, visit http://"+locationServer+":"+str(PORTNUMBER)+"/")
			server.serve_forever()
		except KeyboardInterrupt:
			server.socket.close()

	def kill_child():
		if child_pid is None:
			pass
		else:
			os.kill(child_pid, signal.SIGTERM)

	atexit.register(kill_child)

