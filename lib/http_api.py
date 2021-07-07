import lib.server

from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import requests 
import os

from socketserver import ThreadingMixIn

from time import sleep

import json

class httpApiServer():

	class cameraHTTPSERVER(BaseHTTPRequestHandler):

		def do_GET(self):
			if len(self.path) == 1:
				# this is root.. lets give them index page
				root = os.path.dirname(os.path.abspath(__file__))
				filename = root +'/html/index.html'
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
						if lib.server.hcX.camAvaliable() :
							raw_image = lib.server.hcX.rawImage()
						else :
							raw_image = 0

	                    # transform the byte read into a numpy array
						if len(raw_image) != 0 :
							image =  numpy.fromstring(raw_image, dtype='uint8')

							image = image.reshape((HEIGHT,WIDTH,3))          # Notice how height is specified first and then width
							if opencvFilters:
								image = OpenCvModify.modFilterHills(image, 5) # 4 - 200
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
						try:
							self.wfile.write("--jpgboundary".encode())
							self.send_header('Content-type','image/jpeg')
							self.send_header('Content-length',str(tmpFile.getbuffer().nbytes))
							self.end_headers()
							jpg.save(self.wfile,'JPEG')
						except:
							#print("Client ended session. Doing clean break.")
							break
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
			if self.path.endswith('api/test'):
				self.send_response(200)
				self.send_header('Content-type','application/json')
				self.end_headers()
				checkTest = testSystem.main()
				your_json = '["success '+str(checkTest)+'"]'
				parsed = json.loads(your_json)
				self.wfile.write((json.dumps(parsed, indent=4, sort_keys=True)).encode())
				return

	class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
		"""Handle requests in a separate thread."""
