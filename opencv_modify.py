import cv2
import numpy as np



class OpenCvModify():

	def modFilterHills(img,mod) :
		# Convert unsigned int to float
		hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		img = np.float32(hsvImage)
		H,S,V = cv2.split(hsvImage)
		V = np.clip(V*mod,0,255)
		hsvImage = np.uint8(cv2.merge([H,S,V]))
		rgb = cv2.cvtColor(hsvImage, cv2.COLOR_HSV2BGR)
		return rgb