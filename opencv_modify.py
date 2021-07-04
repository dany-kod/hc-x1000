import cv2
import numpy as np



class OpenCvModify():

	def modBrightness(img,amount) :

		
		# Convert unsigned int to float
		img = np.float32(img)

		# Scale the values so that they lie between [0,1]
		#image = image * scalingFactor

		brightnessOffset = amount

		# Add the offset for increasing brightness
		return img + brightnessOffset