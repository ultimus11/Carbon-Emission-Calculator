import re
import os
import cv2
import time
import pyautogui
import pytesseract
import numpy as np
from PIL import Image
from grabScreen import grab_screen

#Create Black window and show instructions on it
image=np.zeros(shape=[200,800,3],dtype=np.uint8)
textt = "Bring Cursor near to distance Then press P"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,  
	textt,  
	(0, 30),
	font, 0.5,
	(0, 255, 255),
	1,
	cv2.LINE_4)

while True:
	cv2.imshow('frame',image)

	#See if user wants to check again pressing c will clear window
	textt = "Press C to clear screen to check emision again if already checked"
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(image,  
		textt,  
		(0, 150),
		font, 0.5,
		(0, 255, 255),
		1,
		cv2.LINE_4)
	k = cv2.waitKey(0) & 0xFF
	print(k)

	# see if user wants to check emissions
	print(ord('p'))
	if k == ord('p'):
		x,y=pyautogui.position()
		print("ok",x,y)
		x=int(x)-35
		y=int(y)-20
		xx = x+60
		yy = y+20
		capture_screen, image_1=grab_screen(region=(int(x),int(y),xx,yy))
		cv2.imwrite("{}.png".format("woww"),capture_screen)
		text = pytesseract.image_to_string(Image.open("woww.png"))

		#show carbon emissions if some value for distance is extracted through OCR
		try:
			print(text[:3])
			distance = re.findall("\d+\.\d+", text)
			print(distance[0])
			distance = distance[0]
			textt = str((float(distance)*150)/1000)+" Kg of CO2 is going to be emmited for petrol car"
			font = cv2.FONT_HERSHEY_SIMPLEX
			cv2.putText(image,  
				textt,  
				(0, 60),
				font, 0.5,
				(255, 255, 255),
				1,
				cv2.LINE_4)
			textt = str((float(distance)*130)/1000)+" Kg of CO2 is going to be emmited for diesel car"
			font = cv2.FONT_HERSHEY_SIMPLEX
			cv2.putText(image,  
				textt,  
				(0, 95),
				font, 0.5,
				(255, 255, 255),
				1,
				cv2.LINE_4)
			cv2.destroyAllWindows()
		except IndexError:
			pass

	# Check if user wants to exit
	elif k == ord('q'):
		break

	#Clear window if user wants
	elif k == ord('c'):
		image=np.zeros(shape=[200,800,3],dtype=np.uint8)
		textt = "Bring Cursor near to distance Then press P"
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(image,  
			textt,  
			(0, 30),
			font, 0.5,
			(0, 255, 255),
			1,
			cv2.LINE_4)