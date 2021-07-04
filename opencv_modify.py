import cv2
import numpy as np



class OpenCvModify():

	def modBrightness(img,brightnessOffset) :

		
		# Convert unsigned int to float
		img = np.float32(img)

		# Scale the values so that they lie between [0,1]
		#image = image * scalingFactor
		# Add the offset for increasing brightness
		brigthImage = img + brightnessOffset
		return brigthImage