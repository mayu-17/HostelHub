import cv2
import numpy as np 
import pyzbar.pyzbar as pyzbar
import sys
import time
import csv
import base64
from datetime import datetime
from playsound import playsound



cap = cv2.VideoCapture(0)

names=[]
start_hour='12'
start_minute='00'

now=datetime.now()
current_date=now.strftime("%Y-%m-%d")
current_time=now.strftime("%H-%M-%S")
current_hour=datetime.now().hour
current_minute=datetime.now().minute


fob=open('Attendence.csv','a+')

def enterData(z):
   if z in names:
       pass
   else:
      
      names.append(z)
      if int(start_hour)<= current_hour :
         playsound('alert.mpeg')
         names.append(current_date)
      
      
    
      fob.write(z+'   '+current_date+'   '+ current_time +'   '+'\n')
      
      return names
      
      

print("Reading code...............")


def checkData(data):
   try:
      data=str(base64.b64decode(data).decode())
   except(TypeError):
      print('invalid id')
      return
      
    #data=str(data)
   if data in names:
        print('Already present')
   else:
        print('\n'+str(len(names)+1)+'\n'+'Present done')
        enterData(data)   


while True:
   _,frame= cap.read()
   
   
   decodeObject =pyzbar.decode(frame)       
   for obj in decodeObject:
      checkData(obj.data)
      time.sleep(1)

   cv2.imshow('Frame',frame)


   if cv2.waitKey(1)&0xFF == ord('s'):
      cv2.destroyAllWindows()
      break

fob.close()       
